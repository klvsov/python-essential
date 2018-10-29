x, r1, y, r2 = input().split()
x = int(x)
r1 = int(r1)
y = int(y)
r2 = int(r2)

if r1 + r2 <= abs(x - y):
    print(0)
elif r2 - r1 >= abs(x - y):
    print(2)
else:
    print(1)
