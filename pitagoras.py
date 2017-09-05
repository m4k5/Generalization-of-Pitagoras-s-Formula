import math


def pitagoras(s1, s2, a):
    return(math.sqrt(side1 ** 2 + side2 ** 2 -
                     2 * side1 * side2 * math.cos(angle)))


if __name__ = "__main__":
    side1 = int(input("Length of first side:    "))
    side2 = int(input("Length of second side:   "))
    angle = int(input("The angle between them:  "))
    print pitagoras(side1, side2, angle)
