a = input().split()
c = 0
i = 0

for i in range(0, len(a)):
    a[i] = int(a[i])

i = 0

for i in range(1, len(a) - 1):
    if (a[i] > a[i + 1]) and (a[i] > a[i - 1]):
        c += 1
print(c)
