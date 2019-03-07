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
