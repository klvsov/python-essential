n, m, a, b = input().split()
n = int(n)
m = int(m)
a = int(a)
b = int(b)
x = m - n
if x <= 0:
    answer = 0
else:
    if b >= 4 * a:
        answer = a * x
    else:
        answer = (x // 4) * b
        y = x % 4
        if y * a > b:
            answer = answer + b
        else:
            answer = answer + a * y
print(answer)
