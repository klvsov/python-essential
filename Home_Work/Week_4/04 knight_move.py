col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if (abs(col1 - col2) == 2) and (abs(row1 - row2) == 1) or (abs(col1 - col2) == 1) and (abs(row1 - row2) == 2):
    print('YES')
else:
    print('NO')
