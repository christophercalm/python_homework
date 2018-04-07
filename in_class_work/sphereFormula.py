# Program to calculate the volume and surface area of a sphere
import math

r = eval(input("Enter the radius of the sphere: "))

vol = (4/3) * math.pi * (r**3)

area = 4 * math.pi * (r**2)

print("The volume is: ", vol, "The the surface area is: ", area)

