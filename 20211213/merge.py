# [1, 2, 3, 4, [7, 8], [5, 6]...]

import random
L = list(range(16))
random.shuffle(L)
LL = L.copy()  # дополнительная память для сортировки слиянием

def merge(b0, b1, e1):
    b, e0, i = b0, b1, b0  # конец первого массива - начало второго
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
        # возможно, остался незаписанный кусок из наибольших элементов
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]

for p in range(4):
    b = 2 ** (p + 1)
    for i in range(0, len(L), b):  # слияние пар
        merge(i, i + b // 2, i + b)

print(L)
