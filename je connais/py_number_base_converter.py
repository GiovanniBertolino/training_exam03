def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"
    try:
        n = int(number, from_base)
    except ValueError:
        return "ERROR"
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = digits[n % to_base] + res
        n //= to_base
    return res





def main():
    print(number_base_converter("1010", 2, 10))  # Expected: "10"
    print(number_base_converter("FF", 16, 10))  # Expected: "255"
    print(number_base_converter("255", 10, 16))  # Expected: "FF"
    print(number_base_converter("123", 10, 2))  # Expected: "1111011"
    print(number_base_converter("Z", 36, 10))  # Expected: "35"
    print(number_base_converter("35", 10, 36))  # Expected: "Z"
    print(number_base_converter("123", 1, 10))  # Expected: "ERROR"
    print(number_base_converter("G", 16, 10))  # Expected: "ERROR"

if __name__ == "__main__":
    main()
