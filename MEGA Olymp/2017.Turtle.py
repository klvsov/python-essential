n, m, x, y = map(int, input().split())
distance = min(x - 1, y - 1, n - x, m - y)
long = 2 * distance + 1
answer = long ** 2
if x + distance < n:
    answer += long
    if y - distance > 1:
        answer += long + 1
        if x - distance > 1:
            answer += long + 1
print(answer)