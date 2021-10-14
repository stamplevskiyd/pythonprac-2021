from fractions import Fraction
data_list = input().split(', ')
s = data_list[0]
w = data_list[1]
deg1 = int(data_list[2])
deg2 = int(data_list[deg1 + 3])

pol1 = Fraction("0.0")
pol2 = Fraction("0.0")
#print("deg1 = ", deg1)
#print("deg2 = ", deg2)
for i in range(deg1 + 1):
    pol1 += Fraction(data_list[i + 3]) * (Fraction(s) ** (deg1 - i))  # +3, так как 3 лишних символа: w, s, степень первого
#    print(Fraction(data_list[i + 3]))
#print("_"*10)    
for i in range(deg2 + 1):
    pol2 += Fraction(data_list[i + deg1 + 5]) * (Fraction(s) ** (deg2 - i))
#    print(Fraction(data_list[i + deg1 + 5]) )
#print(pol1)
#print(pol2)
#print(w)
#print(pol1/pol2)
#print(pol1/pol2 == w)

def Counter(s, w, *arguments):
    pol1 = s - s # задаем 0 нужного типа
    pol2 = s - s
    for i in range(deg1 + 1):
        pol1 += arguments[i] * (s ** (deg1 - i))
    
