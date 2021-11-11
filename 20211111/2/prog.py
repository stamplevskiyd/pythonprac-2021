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
        square = (max(x1, x2, x3) - min(x1, x2, x3)) * (max(y1, y2, y3) - min(y1, y2, y3)) # не работает
        square -= abs((x1 - x2) * (y1 - y2) / 2) + abs((x3 - x2) * (y3 - y2) / 2) + abs((x1 - x3) * (y1 - y3) / 2)
        if square == 0:
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
        print(s)
        break
