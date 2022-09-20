#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == -10:
    last_digit = 0
else:
    last_digit = number
if last_digit > 5:
    print('Last digit of', number, 'is', last_digit, 'and is greater than 5')
elif last_digit == 0:
    print('Last digit of', number, 'is', last_digit, 'and is 0')
elif last_digit < 6 and last_digit > 0:
    print('Last digit of', number, 'is', last_digit, 'and is less than 6 and not 0')
