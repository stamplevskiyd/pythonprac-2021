from math import sqrt


class SquareIO:
    def __init__(self):
        pass

    def inputCoeff(self, coeff_name):
        coeff_value = input(f"Input {coeff_name}:")
        return coeff_value

    def printResult(self, result):
        print(f"Solution: {result}")


def solveSquare():
    eps = pow(10, -7)
    IO = SquareIO()
    try:
        a = float(IO.inputCoeff("a"))
        b = float(IO.inputCoeff("b"))
        c = float(IO.inputCoeff("c"))
    except Exception:
        IO.printResult("Unable to convert coefficients to float")
    else:
        if abs(a) < eps:
            if abs(b) < eps:  # вырожденное, 5 = 0
                res = None if abs(c) >= eps else (0.0,)
            else:  # bx + c = 0
                res = (- b / c,)  # пусть у программы будет универсальный возвращаемый тип - кортеж
        else:
            dis = b * b - 4 * a * c
            if dis < 0:
                res = None
            elif dis == 0:
                res = (-b / (2 * a), -b / (2 * a))
            else:
                res = ((-b - sqrt(dis)) / (2 * a), (-b + sqrt(dis)) / (2 * a))
        IO.printResult(res)


if __name__ == "__main__":
    solveSquare()  # удобно для тестирования отдельно от unittest