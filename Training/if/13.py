N = int(input())
M = int(input())
x = int(input())
y = int(input())

a = max(N, M)
b = min(N, M)

if x >= b / 2:
    x = b - x
if y >= a / 2:
    y = a - y
if x < y:
    print(x)
else:
    print(y)
