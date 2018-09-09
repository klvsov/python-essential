a = input().split()
i = 0
for i in range(0, len(a)):
    a[i] = int(a[i])
i = 1
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])
