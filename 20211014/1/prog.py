from fractions import Fraction

def Counter(s, w, arguments):  # никак не зависит от типа аргументов
    pol1 = pol2 = s - s # задаем 0 нужного типа (не очень надо, для наглядности)
    deg1 = int(arguments[0])
    deg2 = int(arguments[deg1 + 2])
    for i in range(deg1 + 1):
        pol1 += arguments[i + 1] * (s ** (deg1 - i))
    for i in range(deg2 + 1):
        pol2 += arguments[i + deg1 + 3] * (s ** (deg2 - i))
    return pol1/pol2 == w if pol2 else False

data_list = input().strip().split(',')
for i in range(len(data_list)):  # перевод строк в числа
    data_list[i] = Fraction(data_list[i])
s = data_list[0]
w = data_list[1]
print(Counter(s, w, data_list[2:]))

