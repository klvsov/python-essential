x1,y1,x2,y2,x,y = input().split()
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
x = int(x)
y = int(y)
if (x < x1) and (y > y2):
    print('NW')
elif (x > x2) and (y > y2):
    print('NE')
elif (x < x1) and (y < y1):
    print('SW')
elif (x > x2) and (y < y1):
    print('SE')
elif (y > y2) and (x > x1) and (x < x2):
    print('N')
elif (y < y1) and (x > x1) and (x < x2):
    print('S')
elif (x < x1) and (y > y1) and (y < y2):
    print('W')
elif (x > x2) and (y > y1) and (y < y2):
    print('E')

