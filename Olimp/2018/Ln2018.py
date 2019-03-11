a, b = input().split()
a = int(a)
b = int(b)

c = 0
for i in range(a, b + 1):
    s = 0 #6
    while i > 0:
        s = s + i % 10 #3 #2 #1
        i //= 10 #12 #1 #0
    if s ** 0.5 % 1 == 0:
        c += 1
print(c)    