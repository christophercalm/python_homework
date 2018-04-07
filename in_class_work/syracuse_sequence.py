"""
Christopher Calmes
Program that generates Syracuse Sequence for a given n
Dr. Murimi
04/04/2018
"""

def syr(n):

    num = n
    seq = []

    while num != 1:
        if num % 2 == 0:
            num = num / 2
            seq.append(num)
        else:
            num = 3 * num + 1
            seq.append(num)

    return seq


def main():

    num = eval(input("Enter a number to calculate the syracuse sequence"))
    print(syr(num))