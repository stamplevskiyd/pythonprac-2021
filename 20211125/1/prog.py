import sys
from math import ceil
s = sys.stdin.buffer.read()
count = s[0]
size = ceil((len(s) - 1) / count)
beginning = s[0:1]
s = s[1:]
lines_list = sorted((s[i * size : (i + 1) * size] for i in range(len(s) // size)))
sys.stdout.buffer.write(beginning + b''.join(lines_list))
