from math import sqrt


def solveSquare(a, b, c):
    dis = b * b - 4 * a * c
    if dis < 0:
        return None
    elif dis == 0:
        return -b / (2 * a)
    else:
        return (-b - sqrt(dis)) / (2 * a), (-b + sqrt(dis)) / (2 * a)
