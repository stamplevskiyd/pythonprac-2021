import math

functions = {}
while (data := input().split())[0] != "quit":
    print(functions)
    print(data)
    if data[0][0] == ':':
        functions[data[0][1:]] = (data[0][1:], data[1], data[2])
    else:
        print(functions[data[0]], {functions[data[0]][0]: eval(data[1])})
        print(eval(functions[data[0]], math.__dict__, {functions[data[0]][1]: eval(data[1])}))
print(functions)        
