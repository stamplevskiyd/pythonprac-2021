import math

functions = {}
while (data := input().split())[0] != "quit":
    if data[0][0] == ':':
        for i in range(3, len(data)):  # чтобы можно было писать выражения с пробелами
           data[2] += ' ' + data[i]
        functions[data[0][1:]] = {'new_name': data[0][1:], 'arg': data[1], 'old_name': data[2]}
    else:
        for i in range(2, len(data)):  # чтобы можно было писать выражения с пробелами
           data[1] += ' ' + data[i]
        print(eval(functions[data[0]]['old_name'], {functions[data[0]]['arg']: eval(data[1])}, math.__dict__))
print(len(functions) + 1)

