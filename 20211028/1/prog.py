#1 1 2 3 5 8 13 21

def fib(m:int, n:int):
    digit1, digit2 = 1, 1
    if m < 2:
        yield digit1  # позже сделаю более адекватно
        if m < 1:
            yield digit2
    for i in range(2, m):
        digit1, digit2 = digit2, digit1 + digit2
    for i in range(m, n + 1):
        digit1, digit2 = digit2, digit1 + digit2
        yield digit2

m = int(input())
n = int(input())
gen = fib(m, n)
print(list(gen))
