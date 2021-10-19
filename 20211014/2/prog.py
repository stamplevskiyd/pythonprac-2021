from math import *

def scale(A, B, a, b, x):
    return (x - A) / (B - A) * (b - a) + a

def F(x):
    f = lambda x: eval(data[4])
    return f(x)

# W- ширина, H- высота, А- начало старого отрезка, В- конец старого отрезка

data = list(input().split(" "))
W, H, A, B = int(data[0]), int(data[1]), int(data[2]), int(data[3])
X = [scale(0, W, A, B, i) for i in range(W)]  # перенос точек терминала в координаты
Y = [F(x) for x in X]
my, My = min(Y), max(Y)
Y = [scale(my, My, 0, H, y) for y in Y]  # масштабируем полученные Y
for i in range(len(Y) - 1):
    for j in range(i, len(Y)):
        if Y[i] < Y[j]:
            Y[i], Y[j] = Y[j], Y[i]
            X[i], X[j] = X[j], X[i]

print(X)
print(Y)

index1 = 0
index2 = 0
X = [round(scale(A, B, 0, W, X[i])) if i % 2 else round(scale(A, B, 0, W, X[i])) + 1 for i in range(len(X))]
while True:
    y = Y[index1]
    while index2 < len(X) and y - Y[index2] < W/(2*H):  # ищем иксы с похожими значениями y
        index2 += 1
    similar = sorted([X[i] for i in range(index1, index2)])
    print(' ' * similar[0] + '*', end='')  # пишем первую звездочку в строке
    for i in range(1, index2 - index1):
        print(' ' * (similar[i] - similar[i - 1]) + '*', end='')
    if index2 >= len(X):
        break
    index1 = index2
    print()

