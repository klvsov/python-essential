number = int(input())
i, f1, f2, f = 3, 1, 1, 0
while number >= f:
    f = f1 + f2
    f1 = f2
    f2 = f
    if number == f:
        print(i)
        break
    i += 1
if number < f:
    print(-1)
