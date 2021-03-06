from collections import Counter

W = int(input())
signs = ' ~!@#$%^&*()-_=+\|/]}[{;:\'\",<.>/?\t'  # можно и еще добавить, но вроде хватит
data = []
while True:
    line = input().lower()
    if line.split() == []:
        break
    for sign in signs:
        line = line.replace(sign, '@')
    for word in line.split('@'):
        if word and len(word) == W:
            data.append(word)
c = Counter(data)
if c:
    max_count = c.most_common()[0][1]
    L = sorted([word for word in c if c[word] == max_count])
    for item in L:
        print(item, end=' ')     
