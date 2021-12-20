import itertools

def slide(seq, index):
    seq = itertools.tee(seq, 2)
    yield from itertools.islice(seq[0], index)
    while next(seq[1], None) != None:
        seq = itertools.tee(seq[1], 2)
        yield from itertools.islice(seq[0], index)

import sys
exec(sys.stdin.read())
