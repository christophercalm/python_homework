
# 8/2/2018
# Christopher Calmes
# Program to calculate n roots of a certain number

num = eval(input("Enter the number of which you want to calculate the roots: "))
n = eval(input("Enter the number of roots: "))

for n in range(n):
    root = num ** (1/(n+1))
    print("Root ", n+1, "of ", num, ": ", root)
