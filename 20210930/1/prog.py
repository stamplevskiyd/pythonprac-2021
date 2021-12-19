data = list(eval(input()))
for i in range(len(data) - 1):
    for j in range(len(data) - i - 1):
        if (data[j] ** 2) % 100 > (data[j + 1] ** 2) % 100:
            data[j], data[j + 1] = data[j + 1], data[j]
print(data)            
