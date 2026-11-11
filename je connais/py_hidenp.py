def hidenp(small: str, big: str) -> bool:
    i = 0
    for c in big:
        if i < len(small) and c == small[i]:
            i += 1
    return i == len(small)





def main():
    print(hidenp("abc", "a1b2c3"))  # Expected: True
    print(hidenp("ace", "abcde"))  # Expected: True
    print(hidenp("aec", "abcde"))  # Expected: False
    print(hidenp("", "abc"))  # Expected: True
    print(hidenp("abc", "ab"))  # Expected: False
    print(hidenp("aaaa", "aaa"))  # Expected: False
    print(hidenp("sing","subsequence testing"))  # Expected: True

if __name__ == "__main__":
    main()
