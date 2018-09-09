a = int(input())
i = 0
max = a
b = 0
while a != 0:
    if a > max:
        max = a
        b = i
    i += 1
    a = int(input())
print(b)
