import textdistance as td

def dist(s1, s2, s3):
    if s3 == "L":
        return td.levenshtein(s1, s2)
    elif s3 == "D":
        return td.damerau_levenshtein(s1, s2)
    else:
        return -1

s1 = input()
s2 = input()
s3 = input()
res = dist(s1, s2, s3)
print(res)
