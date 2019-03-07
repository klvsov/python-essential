n, m = input().split()
n = int(n)
m = int(m)

a = []
for i in range(m):
    a.append(int(input()))
a.sort()
res = 0
i = 0
while i < m and n - a[i] >= 0:
    n -= a[i]
    i += 1
    res += 1
print(res)