<<<<<<< HEAD
n, m, x, y = map(int, input().split())

sm = min(x - 1, y - 1, n - x, m - y)

d = sm * 2 + 1

sq = d ** 2

if x + sm < n:
    sq += d
    if y - sm > 1:
        sq += d + 1
        if x - sm > 1:
           sq += d + 1
print(sq)
=======
n = int(input('Введіть число '))
res = 1
for i in range(1, n + 1):
    res *= i
print(res)
>>>>>>> 40f565695b8e91e953f6da39c1dcdd78238fc852
