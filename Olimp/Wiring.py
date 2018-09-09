n, m, a, b = input().split()
n = int(n)
m = int(m)
a = int(a)
b = int(b)

r = 0
 

if (b >= 4 * a):
    r = (m - n) * a
else:
    r = ((m - n) // 4) * b + min (b, ((m - n) % 4) * a)
 
print(r)