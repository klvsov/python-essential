a = input().split()

i = 0

x = int(input())

for i in range(0, len(a)):
    a[i] = int(a[i])

i = 0

count = 1

for i in range(0, len(a)):
    if x <= a[i]:
        count += 1

print(count)
