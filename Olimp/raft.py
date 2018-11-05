h = input().split()
for i in range(len(h)):
    h[i] = int(h[i])

x1 = h[0]
y1 = h[1]
x2 = h[2]
y2 = h[3]
x = h[4]
y = h[5]
answer = ""
if y > y2:
    answer += "N"
if y < y1:
    answer += "S"
if x < x1:
    answer += "W"
if x > x2:
    answer += "E"
