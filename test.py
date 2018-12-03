def isPrime(m):
    prime = True
    d = 2
    while d * d <= m:
        if m % d == 0:
           prime = False
        d += 1
    return prime

m,n = input().split()
m = int(m)
n = int(n)

absent = True

for i in range(m, n + 1):
    if isPrime(i):
        print(i)
        absent = False
    if absent:
        print('Absent')
