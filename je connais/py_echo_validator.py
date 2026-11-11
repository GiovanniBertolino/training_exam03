def echo_validator(text: str) -> bool:
    clean = "".join(c.lower() for c in text if c.isalpha())
    return clean != "" and clean == clean[::-1]








def main():
    print(echo_validator("racecar"))  # Expected: True
    print(echo_validator("A man a plan a canal Panama"))  # Expected: True
    print(echo_validator("race a car"))  # Expected: False
    print(echo_validator("Was it a car or a cat I saw"))  # Expected: True
    print(echo_validator("hello"))  # Expected: False
    print(echo_validator("Madam Im Adam"))  # Expected: True
    print(echo_validator("madam"))  # Expected: True
    print(echo_validator("Able was I ere I saw Elba"))  # Expected: True
    print(echo_validator(""))  # Expected: False

if __name__ == "__main__":
    main()
