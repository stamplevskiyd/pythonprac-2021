import math

functions = {}
counter = 1
while (data := input().split())[0] != "quit":
    counter += 1
    if data[0][0] == ':':
        functions[data[0][1:]] = data[1:]
    else:
        print(eval(functions[data[0]][-1], math.__dict__,
                   {functions[data[0]][i]: eval(data[1 + i]) for i in range(len(data) - 1)}))

print(data[1].format(len(functions) + 1, counter))

