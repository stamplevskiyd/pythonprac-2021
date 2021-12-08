a,b = eval(input())
res = []
for i in range(max(a,2),b):
    for j in range(2, int(i ** 0.5 + 1)):
        if i % j == 0:
            break
    else:
        res.append(i)
print(res)
