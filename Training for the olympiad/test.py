n = int(input())

for i in range(n):
    for j in range(n):
        if n == (i ** j) * (j ** i):
            print(i, j)
            break
