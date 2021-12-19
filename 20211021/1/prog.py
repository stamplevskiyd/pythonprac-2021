line = input().lower()
pairs = set()
index = 0
pair = ''
for letter in line:
    if letter.isalpha():
        pair += letter
        if index == 1:   # добавили первую букву, эта-вторая
            pairs.add(pair)
            index = 1
            pair = letter  # abc -> пары: ab и bc. Последняя букав этой пары - начало следующей
        else:
            index += 1  # эта буква - первая
    else:
        pair = ''
        index = 0
print(pairs)
