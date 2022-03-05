import readline
import shlex

while s := input('> '):
    number, *params = shlex.split(s)
    try:
        number = int(number)
        print(f"< {params[number - 1]}")
    except Exception as E:
        print("Error!")
        break
