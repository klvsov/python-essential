a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

x = a + b + c
y = x // 3
if x % 3 != 0:
    print('IMPOSSIBLE')
else:
    if a > y:
        print('-', a - y, sep="", end=" ")
    elif a < y:
        print('+', y - a, sep="", end=" ")
    else:
        print(0, sep="", end=" ")
    if b > y:
        print('-', b - y, sep="", end=" ")
    elif b < y:
        print('+', y - b, sep="", end=" ")
    else:
        print(0, sep="", end=" ")
    if c > y:
        print('-', c - y, sep="", end=" ")
    elif c < y:
        print('+', y - c, sep="", end=" ")
    else:
        print(0, sep="", end=" ")
