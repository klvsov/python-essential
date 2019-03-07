n = int(input())
a = []
for i in range(n * 2):
    a.append(input())
    a[i] = list(a[i])
    a[i].sort()
for i in range(1, len(a) + 1, 2):
    if a[i] == a[i - 1]:
        print(1)
    else:
        print(0)