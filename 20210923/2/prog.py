sum = 0
while sum <= 21:
    num = int(input())
    if num <= 0:
        print(num)
        break
    else:
        sum += num
else:
    print(sum)
