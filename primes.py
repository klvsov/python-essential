def isPrime(n):
    Prime = True
    d = 2
    while d * d <= n:
        if n % d == 0:
            Prime = False
        d += 1
    return Prime

m, n = input().split()
n = int(n)
m = int(m)
absent = True
for i in range(m, n + 1):
    if isPrime(i):
        print(i)
        absent = False
    if absent:
        print('Absent')
