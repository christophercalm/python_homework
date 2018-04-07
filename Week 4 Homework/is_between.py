'''
Program to determine if a number is between two values
Christopher Calmes
03/27/2018
'''

def is_between(x,y,z):
    try:
        return y < z and y > x
    except TypeError:
        print("You entered the wrong type of data")


print(str(is_between(1,5,7)))
print(str(is_between('a',5,6)))
print(str(is_between(31,5,7)))
print(str(is_between(1,5,4)))
print(str(is_between(1,35,20)))
print(str(is_between(1,5,7)))

