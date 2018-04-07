#Exception Handling

try:
    import moth
except ImportError:
    import math


try:
    fname = "INvalidText.txt"
    infile = open(fname, "r")
except IOError:
    print("The file named is not valid: ")
a = 2
b = "a"
"""
try:
    print (5/0)
except:
    print("You divided by zero")
"""

try:
    print (a/b)
except ZeroDivisionError:
    print("You divided by zero!")
except TypeError:
    print("Division cannot be performed between numeric and string types: ")

try:
    print (math.sqrt(-1))
except ValueError:
    print("Cannot take the square root of a negative number: ")
