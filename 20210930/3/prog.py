first_line = list(eval(input()))
size = len(first_line)
matrix1 = [first_line]
for i in range(size - 1):
    matrix1.append(list(eval(input())))               

first_line = list(eval(input()))
matrix2 = [first_line]
for i in range(size - 1):
    matrix2.append(list(eval(input())))

result = [[0 for i in range(size)] for j in range(size)]

for i in range(size):
    for j in range(size):
        elem = 0
        for k in range(size):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for i in range(size):
    print(result[i])
