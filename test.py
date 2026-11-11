def cryptic_sorter(strings: list[str]) -> list[str]:
    def key(s):
        low = s.lower()
        return (len(s), low, sum(c in "aeiou" for c in low))

    res = strings[:]
    for i in range(len(res)):
        for j in range(len(res) - 1 - i):
            if key(res[j]) > key(res[j + 1]):
                res[j], res[j + 1] = res[j + 1], res[j]
    return res




def main():
    print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))  # Expected: ["cat","dog","apple","banana","elephant"]
    print(cryptic_sorter(["aaa","bbb","AAA","BBB"]))  # Expected: ["aaa", "AAA", "bbb", "BBB"]
    print(cryptic_sorter(["hello","world","hi","test"]))  # Expected: ["hi","test","hello","world"]
    print(cryptic_sorter([]))  # Expected: []
    print(cryptic_sorter([""]))  # Expected: [""]

if __name__ == "__main__":
    main()
