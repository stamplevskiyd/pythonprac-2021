import itertools

def slide(seq, n):
    index = 0
    while index < len(seq):
        yield from itertools.islice(seq, index, n + index)
        index += 1

import sys
exec(sys.stdin.read())
