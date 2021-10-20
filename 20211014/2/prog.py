from math import *

def scale(A, B, a, b, x):
    return (x - A) / (B - A) * (b - a) + a

def F(x):
    f = lambda x: eval(data[4])
    return f(x)

# W- ширина, H- высота, А- начало старого отрезка, В- конец старого отрезка

data = list(input().split(" "))
W, H, A, B = int(data[0]), int(data[1]), float(data[2]), float(data[3])
X = [i for i in range(W)]  # перенос точек терминала в координаты
Y = [F(scale(0, W, A, B, x)) for x in X]
my, My = min(Y), max(Y)
Y = [scale(my, My, 0, H, y) for y in Y]  # масштабируем полученные Y
res = []
for i in range(1, W):
    stars_count = 0
    index2 = ceil(Y[i])
    index1 = ceil(Y[i - 1])
    stars_count += abs(index2 - index1)  # для непрерывности графиков будем заполнять пробелы звездочками
    if stars_count == 0:
        stars_count = 1  # для случая, когда точки близко. чтобы не пропускать координату
    res.append(' ' * index1 + '*' * stars_count)
    res[-1] += ' ' * (H - len(res[-1]))  # строки постоянного размера проще выводить в "повернутом" как надо виде

for i in range(1, H):
    for j in range(W - 1):
        print(res[j][-i], end='')
    print()
