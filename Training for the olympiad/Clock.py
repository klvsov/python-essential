h, m = input().split()
h = int(h)
m = int(m)

v1 = h * 30
v2 = m * 6

if v2 < v1:
    print(int((v1 - v2) / 6))
elif v2 > v1:
    print(int(((360 - v2 + v1) / 6)))
else:
    print(0)
