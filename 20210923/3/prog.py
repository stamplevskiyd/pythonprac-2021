N = int(input())
i, j = N, N
while i < N + 3:
    while j < N + 3:
        copy, sum = i * j, 0
        while copy > 0:
            sum += copy % 10
            copy //= 10
        print(j, "*", i, "=", i*j if sum != 6 else ":=)", sep ='', end=' ')
        j += 1
    print()    
    i += 1
    j = N
