def bracket_validator(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = ""
    for c in s:
        if c in "([{":
            stack += c
        elif c in ")]}":
            if stack == "" or stack[-1] != pairs[c]:
                return False
            stack = stack[:-1]
    return stack == ""





def main():
    print(bracket_validator("()"))  # Expected: True
    print(bracket_validator("()[]{}"))  # Expected: True
    print(bracket_validator("(]"))  # Expected: False
    print(bracket_validator("([)]"))  # Expected: False
    print(bracket_validator("{[]}"))  # Expected: True
    print(bracket_validator("hello(world)"))  # Expected: True
    print(bracket_validator("((())"))  # Expected: False
    print(bracket_validator(""))  # Expected: True

if __name__ == "__main__":
    main()
