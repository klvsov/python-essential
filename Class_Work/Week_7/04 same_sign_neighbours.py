a = input().split()

i = 0

for i in range(0, len(a)):
    a[i] = int(a[i])

i = 0

for i in range(0, len(a) - 1):
    if i <= len(a):
        if (a[i] > 0 and a[i + 1] > 0) or (a[i] < 0 and a[i + 1] < 0):
            print(a[i], a[i + 1])
            break
