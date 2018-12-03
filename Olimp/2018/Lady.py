n, m = input().split()
n = int(n)
m = int(m)

if n > m:
    a = n
    b = m
else:
    a = m
    b = n

d1 = b
d2 = (a - d1) // 2

print(d1, d2)
