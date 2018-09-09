a = input().split()
i = 0
for i in range(0, len(a)):
    a[i] = int(a[i])
    if a[i] % 2 == 0:
        print(a[i])
