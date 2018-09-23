n = 8

x = [0] * n
y = [0] * n

answer = 'NO'

for i in range(n):
    x[i], y[i] = [int(j) for j in input().split()]

for i in range(n):
    for j in range(i+1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            answer = 'YES'

print(answer)
