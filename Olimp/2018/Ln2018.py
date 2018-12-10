a, b = input().split()
a = int(a)
b = int(b)

c = 0
for i in range(a, b + 1):
    s = 0
    while i > 0:
        s += i % 10
        i //= 10
    if s ** 0.5 % 1 == 0:
        c += 1
print(c)
