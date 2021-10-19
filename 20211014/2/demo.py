from math import *

def scale(A, B, a, b, x):
    return (x - A)/(B - A)*(b - a) + a

F = sin
# W- ширина, H- высота, А- начало старого отрезка, В- конец старого отрезка
W, H = 40, 20 #int(input()), int(input())
A, B = -6, 6
X = [scale(0, W, A, B, i) for i in range(W)]  # перенос точек терминала в координаты
Y = [F(x) for x in X]
my, My = min(Y), max(Y)
print(X)
Y = [scale(my, My, 0, H, y) for y in Y]  # масштабируем полученные Y
print(Y)
#X = [round(x) for x in X]
print(X)
print(Y)
print()
for i in range(len(Y) - 1):
    for j in range(i, len(Y)):
        if Y[i] < Y[j]:
            Y[i], Y[j] = Y[j], Y[i]
            X[i], X[j] = X[j], X[i]

print(X)
print(Y)

for x in X:
    print(' ' * round(scale(A, B, 0, W, x)) + '*')
