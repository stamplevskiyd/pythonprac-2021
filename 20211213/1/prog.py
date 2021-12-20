# комментарии с семинара оставлю, так нагляднее

# [1, 2, 3, 4, [7, 8], [5, 6]...]

import random
import asyncio
from collections import defaultdict

# Тапкая вот пилюлька волшебная помогла
# E = defaultdict(asyncio.Event)

#L = list(range(16))
#random.shuffle(L)
#LL = L.copy()  # дополнительная память для сортировки слиянием


async def merge(b0, b1, e1, n, event_left, event_right, new_event):
    await event_left.wait()
    await event_right.wait()
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
    await asyncio.sleep(0)  # возвращает управление в mainloop, а потом обратно
    # но за это время другие задания могли изменить массив.
    # print(f"-> {n}")
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    new_event.set()


async def joiner():
    tasks = []
    events = defaultdict(asyncio.Event)
    n = 0
    for p in range(4):
        b = 2 ** (p + 1)
        for i in range(0, len(L), b):  # слияние пар
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, n, events[(p, i)], events[(p, (i + b) // 2)], events[(p + 1, i)])))

    for i in range(16):
        events[(0, i)].set()
    await asyncio.gather(*tasks)

L = eval(input())
LL = L.copy()  # дополнительная память для сортировки слиянием

asyncio.run(joiner())
print(L)
