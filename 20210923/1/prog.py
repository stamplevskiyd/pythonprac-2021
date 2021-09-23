num = int(input())
if num % 2 == 0 and num % 25 == 0:
    print("A +", end=' ')
else:
    print("A -", end=' ')
if num % 2 == 1 and num % 25 == 0:
    print("B +", end=' ')
else:
    print("B -", end=' ')
if num % 8 == 0:
    print("C +", end=' ')
else:
    print("C -", end=' ')
