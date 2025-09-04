# binary_to_decimal.py

binary = input("Enter a binary number: ")

try:
    decimal = 0
    power = 0
    # Process each digit from right to left
    for digit in reversed(binary):
        if digit not in ('0', '1'):
            raise ValueError("Invalid binary number")
        decimal += int(digit) * (2 ** power)
        power += 1
    print(f"Decimal representation: {decimal}")
except ValueError as e:
    print(e)
