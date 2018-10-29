m, k = input().split()
m = int(m)
k = int(k)
if k % 2 == 0:
    s = 0
else:
    s = m
res = ""
while s <= k * m:
    res = res + str(s) + ' '
    s = s + 2 * m

print(res)
