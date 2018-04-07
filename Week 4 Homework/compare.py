'''
Program to compare x with another number
Christopher Calmes
/03/27/2018
'''

def cmp(x: int, y: int):
    try:
        if x > y: return 1
        elif x == y: return 0
        elif x < y: return -1
    except OverflowError:
        print("The value entered was too large")

print(cmp(1,5))
print(cmp(5,10))
print(cmp((5*10 ** 1000), 12))
print(cmp(10,10))
