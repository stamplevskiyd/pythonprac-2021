from math import *

class InvalidInput(Exception):
    pass
class BadTriangle(Exception):
    pass

def TriangleSquare(data):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(data)
    except Exception as E:
        raise InvalidInput
    else:
        try:
            for coordinate in [x1, x2, x3, y1, y2, y3]:  # int или bool то приведутся к float, а complex/str/...-нет
                float(coordinate)
        except Exception:
            raise BadTriangle
        A = dist((x1, y1), (x2, y2))
        B = dist((x1, y1), (x3, y3))
        C = dist((x3, y3), (x2, y2))
        p = (A + B + C) / 2
        square = sqrt(p*(p - A) * (p - B) * (p - C))
        if square <= 0:
            raise BadTriangle
        return square

while True:
    try:
        s = TriangleSquare(input())
    except BadTriangle:
        print("Not a triangle")
    except InvalidInput:
        print("Invalid input")
    else:
        print(f"{s:.2f}")
        break
