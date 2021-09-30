data = list(eval(input()))
for i in range(len(data) - 1):
    for j in range(i,len(data)):
        if (data[i] ** 2) % 100 > (data[j] ** 2) % 100:
            data[i], data[j] = data[j], data[i]
print(data)            
