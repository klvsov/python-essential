m, n = input().split()
n = int(n)
m = int(m)
c = 0

for i in range(m, n + 1):
    if m <= 10:

        if i / 2 == 1:
            print('2')
            c += 1

        elif i / 3 == 1:
            print('3')
            c += 1

        if (i % 2 == 0) or (i % 3 == 0):
            continue

    elif (i % 2 == 0) or (i % 10 == 5) or (i % 3 == 0) or (i % 7 == 0):
        continue
    print(i)
    c += 1

if c == 0:
    print('Absent')
