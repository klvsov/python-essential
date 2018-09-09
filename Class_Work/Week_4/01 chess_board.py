c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if c1 % 2 == 0 and r1 % 2 == 0 or c1 % 2 != 0 and r1 % 2 != 0:
    cell1 = 'b'
else:
    cell1 = 'w'

if c2 % 2 == 0 and r2 % 2 == 0 or c2 % 2 != 0 and r2 % 2 != 0:
    cell2 = 'b'
else:
    cell2 = 'w'

if cell1 == cell2:
    print('YES')
else:
    print('NO')
