#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

l_d = abs(number) % 10

if l_d > 5:
    print(f"Last digit of {number:d} is {l_d:d} and is greater than 5", end=" ")
elif l_d == 0:
    print(f"Last digit of {number:d} is {l_d:d} and is 0", end=" ")
elif l_d < 6 and l_d != 0:
    print(f"Last digit of {number:d} is {l_d:d} and is less than 6 and not 0", end=" ")
