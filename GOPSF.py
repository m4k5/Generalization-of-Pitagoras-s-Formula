import math

a = input("Length of first side:    ")
b = input("Length of second side:   ")
d = input("The angle between them:  ")

side1 = int(a)
side2 = int(b)
angle = int(d)

answer = math.sqrt(side1*side1 + side2*side2 - 2*side1*side2*math.cos(angle))
print(answer)
