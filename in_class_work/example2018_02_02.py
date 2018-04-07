# Class notes for 02/02/2018
# Accept a number from the user. Print all even numbers up to that number
# for var in range()


n = eval(input("Enter a number to count to: "))
for i in range(0,n+1,2): 
    print (i, end=" ")
