from random import randint

num = int(input())
position = randint(0, 9)  # выбор позиции, на которую будет поставлено заданное число
res_list = [randint(1, 100) for i in range(9)]  # создание остального списка
res_list.insert(position, num)  # Добавление элемента на выбранную позицию
print(res_list)

