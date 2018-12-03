a1, a2, a3 = input().split()
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
s = a1 + a2 + a3
if s % 3 == 0:
    d = s // 3
    if a1 - d > 0:
        print('-', a1 - d, sep="", end=" ")
    elif a1 - d < 0:
        print('+', d - a1, sep="", end=" ")
    else:
        print(0, sep="", end=" ")
    if a2 - d > 0:
        print('-', a1 - d, sep="", end=" ")
    elif a2 - d < 0:
        print('+', d - a2, sep="", end=" ")
    else:
        print(0, sep="", end=" ")
    if a3 - d > 0:
        print('-', a3 - d, sep="", end=" ")
    elif a3 - d < 0:
        print('+', d - a3, sep="", end=" ")
    else:
        print(0, sep="", end=" ")
else: print ('IMPOSSIBLE')
