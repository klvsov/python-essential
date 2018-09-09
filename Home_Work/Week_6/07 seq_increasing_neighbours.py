count = 0
a = int(input())
while a != 0:
    b = a
    a = int(input())
    if a > b:
        count += 1
print(count)
