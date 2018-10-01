n = int(input())

a = input().split()

for i in range(n):
    a[i] = int(a[i])

col_1 = col_2 = col_3 = col_4 = col_5 = col_6 = col_7 = col_8 = 0

for i in range(n):
    if a[i] == 1:
        col_1 += 1

    if a[i] == 2:
        col_2 += 1

    if a[i] == 3:
        col_3 += 1

    if a[i] == 4:
        col_4 += 1

    if a[i] == 5:
        col_5 += 1

    if a[i] == 6:
        col_6 += 1

    if a[i] == 7:
        col_7 += 1

    if a[i] == 8:
        col_8 += 1

print(1, col_1, 2, col_2, 3, col_3, 4, col_4, 5, col_5, 6, col_6, 7, col_7, 8, col_8)
