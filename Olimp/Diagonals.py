n = int(input())

if n == 3:
    answer = 0
else:
    answer = 1
    k = n - 3
    for i in range(k, n + 1):
        answer = answer * i
    answer = answer / 24

print(int(answer))
