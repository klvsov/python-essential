x1, r1, x2, r2 = input().split()
x1 = int(x1)
r1 = int(r1)
x2 = int(x2)
r2 = int(r2)

d = abs(x1 - x2)

if r1 + r2 <= d:
    print(0)
elif r2 - r1 >= d:
    print(2)
else:
    print(1)
