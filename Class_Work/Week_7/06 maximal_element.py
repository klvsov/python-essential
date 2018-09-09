a = input().split()
i = 0
for i in range(0, len(a)):
    a[i] = int(a[i])

max = a[0]

i = 0
n = 0

for i in range(1, len(a)):
    if a[i] > max:
        max = a[i]
        n = i

print(max, n)
