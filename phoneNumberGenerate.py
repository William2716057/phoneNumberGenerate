import random

#mobile = input("Mobile: Y/N")
#landline = 
#country_prefix = input("Include country prefix? ")

quantity = int(input("How many numbers? "))
prefix = "021"
prefix2 = "022"
prefix3 = "027"
for _ in range(quantity):
    number = random.randint(100000, 999999)
    
    print(f"{prefix} {number}")