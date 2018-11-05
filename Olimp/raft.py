x1, y1, x2, y2, x, y = input().split()
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
x = int(x)
y = int(y)

answer = ''
if y > y2:
    answer += 'N'
if y < y1:
    answer += 'S'
if x < x1:
    answer += 'W'
if x > x2:
    answer += 'E'

print(answer)
