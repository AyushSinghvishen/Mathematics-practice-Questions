# sum_of_even_numbers_simple.py

n = int(input("Enter the number of even natural numbers to sum: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    total = 0
    for i in range(1, n + 1):
        total += 2 * i  # 2, 4, 6, ...
    print(f"The sum of the first {n} even natural numbers is: {total}")
