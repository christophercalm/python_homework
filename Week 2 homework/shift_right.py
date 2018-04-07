# Program to shift a string to the right by a specified amount
# Christopher Calmes
# 02/21/2018

def main():
    
    ip=input("Enter a word: ")
    shift = eval(input("Enter the amount of shift: "))

    shift %= len(ip)


    p1 = ip[len(ip) - shift:] #first part of string
    p2 = ip[:len(ip) - shift] #second part of string


    ip = p1 + p2
    print (ip)


if __name__ == "__main__":
    main()
