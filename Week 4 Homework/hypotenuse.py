'''
Program to compute the hypotenuse given two legs
Christopher Calmes
03/27/2018
'''

import math

def hypotenuse(leg1, leg2):
    try:
        return math.sqrt(leg1**2 + leg2 ** 2)
    except ArithmeticError:
        print("Bad values")


print(hypotenuse(3,4))
print(hypotenuse(3.001,4))

    
