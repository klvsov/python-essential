a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

s = a + b + c
x = s / 3

if x % 1 != 0:
    print('IMPOSSIBLE')
else:
    x = int(x)
    if a > x:
        print('-', a - x, sep="", end=" ")
    elif a < x:
        print('+', x - a, sep="", end=" ")
    else:
        print(0, sep="", end=" ")
    if b > x:
        print('-', b - x, sep="", end=" ")
    elif b < x:
        print('+', x - b, sep="", end=" ")
    else:
        print(0, sep="", end=" ")
    if c > x:
        print('-', c - x, sep="", end=" ")
    elif c < x:
        print('+', x - c, sep="", end=" ")
    else:
        print(0, sep="", end=" ")
