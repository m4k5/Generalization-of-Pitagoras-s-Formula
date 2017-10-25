import math


def pitagoras(s1, s2, a):
    return(math.sqrt(s1 ** 2 + s2 ** 2 -
                     2 * s1 * s2 * math.cos(a)))


if __name__ = "__main__":
    side1 = int(input("Length of first side:    "))
    side2 = int(input("Length of second side:   "))
    angle = int(input("The angle between them:  "))
    print pitagoras(side1, side2, angle)
