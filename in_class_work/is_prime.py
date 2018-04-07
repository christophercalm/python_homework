"""
Program to check if a certain number is prime
Christopher Calmes
Dr. Murimi
04/04/2018
"""

import math

divisors = []
def is_prime(n):

    if n == 1 or n == 2 or n == 3:
        return True

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            return False
            break

    return True


def goldbach(t):

    pairs = []
    for k in range(2, int((t/2)) + 1):

        if is_prime(k) and is_prime(t-k):

            print("Found a pair")
            pairs.append((k, t-k))

    return pairs

def main():

    limit = eval(input("Enter a number: "))
    if is_prime(limit):
        print(str(limit))

    print(goldbach(limit))


main()