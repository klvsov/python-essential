d = [int(i) for i in input().split()]
V = d[1]

del d[0]
del d[1]

k = 0
count = 0
for i in range(len(d)):
    if d[i] > V:
        k = i
        break

for i in range(len(d)):
    if d[i] > V:
        count += 1

if k == 0:
    print(0)
else:
    print(1, k + 1, count)
