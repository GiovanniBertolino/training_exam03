def string_sculptor(text: str) -> str:
    res = ""
    n = 0
    for c in text:
        if c.isalpha():
            res += c.lower() if n % 2 == 0 else c.upper()
            n += 1
        else:
            res += c
    if res == "":
        return '""'
    return res






def main():
    print(string_sculptor("hello"))  # Expected: "hElLo"
    print(string_sculptor("Hello World"))  # Expected: "hElLo WoRlD"
    print(string_sculptor("   hello   "))  # Expected: "   hElLo   "
    print(string_sculptor("abc123def"))  # Expected: "aBc123DeF"
    print(string_sculptor("Python3.9!"))  # Expected: "pYtHoN3.9!"
    print(string_sculptor(""))  # Expected: ""

if __name__ == "__main__":
    main()
