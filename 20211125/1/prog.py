import sys
s = sys.stdin.buffer.readline()
count = s[0]
size = (len(s) - 1) // count + 1
lines_list = sorted((s[i * size : (i + 1) * size] for i in range(len(s) // size)))
sys.stdout.buffer.write(s[0:1] + b''.join(lines_list) + b'\n')
