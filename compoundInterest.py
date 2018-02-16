# 08/02/2018
# Christopher Calmes
# Program to calculate annual compound interest

p = eval(input("Enter the principal investment amount: "))
r = eval(input("Enter the annual interest rate: "))
n = eval(input("Enter the number of times that interest is compounded: "))
t = eval(input("Enter the number of years that the money is invested: "))

a = p * ((1 + (r / n)) ** (n * t))

print ("The future value of the investment is: ", a)
print ("The amount of interest compounded is: ", a - p)

