#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if last > 5 and number > 0:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last < 6 and last != 0 and number > 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
if number < 0 and last < 6 and last != 0:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
elif number < 0 and last > 5:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
