def Pareto(*data):
    res = ()
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i][0] <= data[j][0] and data[i][1] <= data[j][1]\
               and (data[i][0] < data[j][0] or data[i][1] < data[j][1]):
                break
        else:
            res = res + (data[i],)
    return res        

# для тестов
print(Pareto(*(eval(input()))))
