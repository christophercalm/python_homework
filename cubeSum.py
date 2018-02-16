# Find the sum of the cubes of the friust n natural numbers, where n is a value supplied by the user

import math

n = eval(input("Enter how many natural numbers to calculate: " ))

acc = 0
for i in range(n):
    acc += i**3

print(acc)

