a = int(input())
max = a
count = 1
while a != 0:
    a = int(input())
    if a > max:
        max = a
        count = 1
    else:
        if a == max:
            count += 1
print(count)
