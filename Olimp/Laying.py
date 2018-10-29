s, n = input().split()
s = int(s)
n = int(n)

a = input().split()

for i in range(len(a)):
    a[i] = int(a[i])
s1 = 0
s2 = 0
for i in range(n):
    x = a[i]
    if s1 + x <= s:
        s1 += x
    else:
        s2 += x
print(s1, s2)


