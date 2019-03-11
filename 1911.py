m = int(input())
n = int(input())

for i in range(m, n + 1):
    if (i % 2 == 0) or (i % 10 == 5) or (i % 3 == 0) or (i % 7 == 0):
        continue
    print(i)
