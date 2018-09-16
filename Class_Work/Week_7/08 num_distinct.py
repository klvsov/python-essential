a = input().split()


for i in range(0, len(a)):
    a[i] = int(a[i])

i = 0

count = 1

for i in range(0, len(a)-1):
    if a[i] != a[i+1]:
        count += 1

print(count)
