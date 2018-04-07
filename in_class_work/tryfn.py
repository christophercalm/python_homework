num1 = 4
num2 = 4

def addnum():
        total = num1 + num2
        print(total)

addnum()

def addNumbers(n1,n2):
    print (n1+n2)

addNumbers(6,98)

def countTo(x,y):
    for i in range(x+1,y):
        print(i)
            

countTo(5,10)

def doubleLetter(string):
    oString = ""
    for letter in string:
        oString += 2*letter
    return oString

print(doubleLetter("Hello World"))

def squareNums(nums):
    squareNum = []
    for i in nums:
        squareNum.append(i**2)
    return squareNum

mylist = [1,3,4,5,68,23,45]

print(squareNums(mylist))

def whoWins(team1, score1, team2, score2):
    if score1 > score2:
        return (team1 + "scored: " + str(score1) + "points and beat: " + team2 + "by: " + str(score1 - score2))
    elif score2 > score1:
        return (team2 + "scored: " + str(score2) + "points and beat: " + team1 + "by: " + str(score2 - score1))
    else:
        return(team1 + "and " + team2 + "tied!")

print(whoWins("OU", 50, "OSU", 20))
