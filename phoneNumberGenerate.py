import random

quantity = int(input("How many numbers? "))
prefixes = ["021", "022", "027"]

produce_numbers = lambda prefix: [print(f"{prefix} {random.randint(1000000000, 9999999999)}") for i in range(quantity)]

for prefix in prefixes:
    produce_numbers(prefix)