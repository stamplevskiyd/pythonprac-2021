import sys
s = sys.stdin.buffer.read()
count = s[0]
beginning = s[0:1]
s = s[1:]
lines_list = sorted((s[i * len(s) // count : (i + 1) * len(s) // count] for i in range(0, count, 1)))
sys.stdout.buffer.write(beginning + b''.join(lines_list))
