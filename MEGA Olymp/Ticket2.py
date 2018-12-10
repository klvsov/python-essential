x, y = input().split()
x = int(x)
y = int(y)

s1 = 3 * x + 2 * y
s2 = 40 + 2 * y
s3 = 30 + 3 * x
s4 = 60

print(min(s1, s2, s3, s4))
