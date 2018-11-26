V = int(input())
answer = V / 4

if V % 4 != 0:
    answer += 1

print(int(answer))
