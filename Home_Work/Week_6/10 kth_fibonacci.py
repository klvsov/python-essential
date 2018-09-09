need_number = int(input())
f1, f2, f, i = 1, 1, 0, 2
if need_number == 2:
    print(1)
else:
    while i != need_number:
        if need_number == 1:
            f = 1
            break
        elif need_number == 0:
            break
        else:
            f = f1 + f2
            f1 = f2
            f2 = f
            i += 1
    print(f)
