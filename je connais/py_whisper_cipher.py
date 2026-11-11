def whisper_cipher(text: str, shift: int) -> str:
    res = ""
    for c in text:
        if 'a' <= c <= 'z':
            res += chr((ord(c) - 97 + shift) % 26 + 97)
        elif 'A' <= c <= 'Z':
            res += chr((ord(c) - 65 + shift) % 26 + 65)
        else:
            res += c
    if res == "":
        return '""'
    return res




def main():
    print(whisper_cipher("hello", 3))  # Expected: "khoor"
    print(whisper_cipher("Hello World!", 1))  # Expected: "Ifmmp Xpsme!"
    print(whisper_cipher("xyz", 3))  # Expected: "abc"
    print(whisper_cipher("ABC123def", 5))  # Expected: "FGH123ijk"
    print(whisper_cipher("", 10))  # Expected: ""
    print(whisper_cipher("abc", -3))  # Expected: "xyz"

if __name__ == "__main__":
    main()
