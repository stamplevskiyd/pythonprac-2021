

import random
import asyncio
from collections import defaultdict
import math



async def merge(b0, b1, e1, n, event_left, event_right, new_event):
    await event_left.wait()
    await event_right.wait()
    b, e0, i = b0, b1, b0  # конец первого массива - начало второго
    b1, e1 = min(b1, len(L)), min(e1, len(L))  # чтобы не выходить за пределы массива
    while b0 < e0 and b1 < e1:
        if L[b0] < L[b1]:
            LL[i] = L[b0]
            b0 += 1
        else:
            LL[i] = L[b1]
            b1 += 1
        i += 1
    await asyncio.sleep(0)

    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    new_event.set()


async def joiner():
    tasks = []
    events = defaultdict(asyncio.Event)
    n = 0
    new_deg = math.ceil(math.log2(len(L)))  # для например 40 элементов надо массив на 64, то есть степень = 6
    for p in range(new_deg):
        b = 2 ** (p + 1)
        for i in range(0, len(L), b):  # слияние пар. дальше len(L) идти бессмысленно
            tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, n, events[(p, i)], events[(p, i + b // 2)], events[(p + 1, i)])))

    for pair in events:
        if pair[1] >= len(L) or pair[0] == 0:
            events[pair].set()
    await asyncio.gather(*tasks)

L = eval(input())
LL = L.copy()  # дополнительная память для сортировки слиянием

asyncio.run(joiner())
print(L)
