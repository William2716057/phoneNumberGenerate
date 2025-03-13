import random


quantity = int(input("How many numbers? "))
prefixes = ["021", "022", "027"]

for prefix in prefixes:
    for _ in range(quantity):
        number = random.randint(1000000000, 9999999999)  # Generate a 10-digit number
        print(f"{prefix} {number}")
