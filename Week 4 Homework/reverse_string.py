'''
Program to reverse a string
Christopher Calmes
03/27/2018
'''

def reverse(s):
    reversed = ''
    try:
        for c in range(len(s), 0, -1):
            reversed += s[c-1]
        for i in reversed:
            print(i)
    except KeyboardInterrupt:
        print("Program Cancelled")

reverse("Hello World")
reverse("Apache Helicopter")

    
