import math

side1 = int(input("Length of first side:    "))
side2 = int(input("Length of second side:   "))
angle = int(input("The angle between them:  "))

print(math.sqrt(side1 ** 2 + side2 ** 2 - 2 *
                side1 * side2 * math.cos(angle)))
