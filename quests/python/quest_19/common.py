def mix(a: str, b: str) -> str:
    if "K" in {a, b}:
        return "K"
    if {a, b} == {"C", "M"}:
        return "B"
    if {a, b} == {"C", "Y"}:
        return "G"
    if {a, b} == {"M", "Y"}:
        return "R"
    return a
