a, b, h = input().split()

a = int(a)
b = int(b)
h = int(h)

s1 = a * b
s2 = (a - 2 * h) * (b - 2 * h)
s = s1 - s2
print(s)
