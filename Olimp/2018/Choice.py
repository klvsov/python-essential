x1, y1, x2, y2, x3, y3 = input().split()

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
x3 = int(x3)
y3 = int(y3)

if x1 == x2:
    x = x3
elif x1 == x3:
    x = x2
else:
    x = x1

if y1 == y2:
    y = y3
elif y1 == y3:
    y = y2
else:
    y = y1

print(x, y)
