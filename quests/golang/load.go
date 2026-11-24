package lotw

import (
	"bufio"
	"bytes"
	"crypto/aes"
	"crypto/cipher"
	"encoding/hex"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"os"
	"time"

	"github.com/joho/godotenv"
)

func ReadLines(file *os.File) []string {
	var result []string = []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		result = append(result, scanner.Text())
	}
	file.Close()
	return result
}

type EverybodyCodesAPI struct {
	client *http.Client
	cookie string
	seed   int
}

type ProfileResponse struct {
	Seed int `json:"seed"`
}

type KeyedResponse struct {
	K1 string `json:"key1"`
	K2 string `json:"key2"`
	K3 string `json:"key3"`
}

func keymap(k KeyedResponse) map[int]string {
	return map[int]string{
		1: k.K1,
		2: k.K2,
		3: k.K3,
	}
}

func MakeEverybodyCodesAPI() (*EverybodyCodesAPI, error) {
	if err := godotenv.Load(); err != nil {
		return nil, err
	}

	var cookie string = os.Getenv("SESSION")

	jar, err := cookiejar.New(nil)
	if err != nil {
		return nil, err
	}

	u, _ := url.Parse("https://everybody.codes")
	jar.SetCookies(u, []*http.Cookie{
		{Name: "everybody-codes", Value: cookie, Domain: "everybody.codes", Path: "/"},
	})

	var api *EverybodyCodesAPI = &EverybodyCodesAPI{
		client: &http.Client{
			Jar:     jar,
			Timeout: 10 * time.Second,
		},
		cookie: cookie,
		seed:   -1,
	}

	// Get seed
	resp, err := api.client.Get("https://api.everybody.codes/user/me")
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, errors.New(resp.Status)
	}

	var response ProfileResponse
	if err := json.NewDecoder(resp.Body).Decode(&response); err != nil {
		return nil, err
	}

	if response.Seed == -1 {
		return nil, errors.New("no seed")
	}

	api.seed = response.Seed

	return api, nil
}

func MustEverybodyCodesAPI() *EverybodyCodesAPI {
	api, err := MakeEverybodyCodesAPI()
	if err != nil {
		log.Fatal(err)
	}
	return api
}

func (api *EverybodyCodesAPI) getAESKeys(quest int) (*KeyedResponse, error) {
	resp, err := api.client.Get(fmt.Sprintf("https://api.everybody.codes/event/2026/quest/%d", quest))
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, errors.New(resp.Status)
	}

	var keys KeyedResponse
	if err := json.NewDecoder(resp.Body).Decode(&keys); err != nil {
		return nil, err
	}

	return &keys, nil
}

func decrypt(key string, eInput string) ([]byte, error) {
	block, err := aes.NewCipher([]byte(key))
	if err != nil {
		return nil, err
	}

	ciphertext, err := hex.DecodeString(eInput)
	if err != nil {
		return nil, err
	}
	if len(ciphertext)%aes.BlockSize != 0 {
		return nil, fmt.Errorf("ciphertext is not a multiple of the block size")
	}

	iv := []byte(key[:16])
	padded := make([]byte, len(ciphertext))
	cipher.NewCBCDecrypter(block, iv).CryptBlocks(padded, ciphertext)

	return pkcs7Unpad(padded, aes.BlockSize)
}

func pkcs7Unpad(data []byte, blockSize int) ([]byte, error) {
	if len(data) == 0 || len(data)%blockSize != 0 {
		return nil, errors.New("invalid padded length")
	}
	n := int(data[len(data)-1])
	if n == 0 || n > blockSize {
		return nil, errors.New("invalid padding")
	}
	if !bytes.Equal(data[len(data)-n:], bytes.Repeat([]byte{byte(n)}, n)) {
		return nil, errors.New("invalid padding")
	}
	return data[:len(data)-n], nil
}

func (api *EverybodyCodesAPI) decryptInputs(encrypted map[int]string, keys KeyedResponse) (map[int]string, error) {
	result := make(map[int]string, len(encrypted))

	for problem, key := range keymap(keys) {
		eInput, ok := encrypted[problem]
		if !ok || key == "" { // part not unlocked yet
			continue
		}

		decrypted, err := decrypt(key, eInput)
		if err != nil {
			return nil, fmt.Errorf("part %d: %w", problem, err)
		}
		result[problem] = string(decrypted)
	}
	return result, nil
}

func (api *EverybodyCodesAPI) MustInput(quest int) map[int]string {
	resp, err := api.client.Get(fmt.Sprintf("https://everybody.codes/assets/2026/%d/input/%d.json", quest, api.seed))
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		log.Fatalf("input: %s", resp.Status)
	}

	var encrypted map[int]string
	if err := json.NewDecoder(resp.Body).Decode(&encrypted); err != nil {
		log.Fatal(err)
	}

	keys, err := api.getAESKeys(quest)
	if err != nil {
		log.Fatal(err)
	}

	inputs, err := api.decryptInputs(encrypted, *keys)
	if err != nil {
		log.Fatal(err)
	}
	return inputs
}
