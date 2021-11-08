def fib(m: int, n: int):
    digit1, digit2 = 1, 0
    for i in range(0, n + 1):
        digit1, digit2 = digit2, digit1 + digit2
        if i >= m:
            yield digit2

import sys
exec(sys.stdin.read())
