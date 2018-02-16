# Program to calculate accuracy and precision of a test
# Christopher Calmes
# 02/09/2017

fp = eval(input("Enter the number of false positives: "))
tp = eval(input("Enter the number of true positives: "))
fn = eval(input("Enter the number of false negatives: "))
tn = eval(input("Enter the number of true negatives: "))

accuracy = (tp + tn)/(tp + tn + fp + fn)

print("The accuracy of the test is: ", accuracy)

precision = (tp)/(tp + fn)

print("The precision of the test is: ", precision)
