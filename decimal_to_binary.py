# decimal_to_binary.py

num = int(input("Enter a decimal number: "))

if num < 0:
    print("Please enter a non-negative number.")
else:
    binary = ""
    if num == 0:
        binary = "0"
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

    print(f"Binary representation: {binary}")
