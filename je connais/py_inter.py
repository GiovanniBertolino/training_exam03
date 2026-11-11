def inter(s1: str, s2: str) -> str:
    res= ""
    for c in s1:
        if c in s2 and c not in res:
            res += c
    if s1 == "" or s2 == "" or res == "":
        return '""'
    return res






def main():
    print(inter("hello", "world"))  # Expected: "lo"
    print(inter("banana", "band"))  # Expected: "ban"
    print(inter("abcabc", "bc"))  # Expected: "bc"
    print(inter("abc", "xyz"))  # Expected: ""
    print(inter("", "abc"))  # Expected: ""

if __name__ == "__main__":
    main()
