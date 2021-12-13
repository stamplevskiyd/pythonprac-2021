# [1, 2, 3, 4, [7, 8], [5, 6]...]

import random
import asyncio

#Тапкая вот пилюлька волшебная помогла
#E = defaultdict(asyncio.Event) 

L = list(range(16))
random.shuffle(L)
LL = L.copy()  # дополнительная память для сортировки слиянием

async def merge(b0, b1, e1, n, event_left, event_right, new_event):
    await event_left
    await event_right
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
    #print(f"-> {n}")
    LL[i:e1] = L[b0:e0] + L[b1:e1]
    L[b:e1] = LL[b:e1]
    new_event.set()

async def joiner():
    tasks = []
    n = 0
    for p in range(4):
        b = 2 ** (p + 1)
        for i in range(0, len(L), b):  # слияние пар
            if p == 0:
                event_left = asyncio.Event()  # на первом шаге создадим события, а дальше пусть сами генерируются
                event_right = asyncio.Event()
                new_event = asyncio.Event()
                tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, n, event_left, event_right, new_event)))
            else:    
                #tasks.append(asyncio.create_task(merge(i, i + b // 2, i + b, n, event_left, event_right)))
            n += 1
    await asyncio.gather(*tasks)  
            
asyncio.run(joiner())
print(L)
