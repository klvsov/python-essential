d = int(input())
if (d >= 1) and (d <= 100):
    if (d >= 11) and (d <= 19) or (d % 10 == 0):
        print(d, 'днів')
    elif d % 10 == 1:
        print(d, 'день')
    elif (d % 10 >= 2) and (d % 10 <= 4):
        print(d, 'дні')
    else:
        print(d, 'днів')
