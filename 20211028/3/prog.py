import itertools

print(", ".join(sorted(["".join(list(word)) for word in list(itertools.product('TOR', repeat=eval(input()))) if "".join(list(word)).count('TOR') == 2])))
