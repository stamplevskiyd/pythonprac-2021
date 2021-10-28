import itertools

def slide(seq, n):
    index = 0
    while True:
        yield from itertools.islice(seq, index, n + index)
        index += 1

n = int(input())
data = input().split()
s = slide(data, n)
for i in range(20):
    print(next(s), end=' ')
