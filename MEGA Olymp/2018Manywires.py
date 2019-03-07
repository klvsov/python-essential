n = int(input())
m = int(input())
a = []
for i in range(n):
    row = input().split()
    a.append(row)
answer = []
for i in range(n):
    if a[i] != '.':
        answer.append(i + 1)
for i in range(1, n):
    for j in range(m):
        if a[i][j] == '/' or a[i][j] == ')':
            answer[i] -= 1
        if a[i][j] == "\\" or a[i][j] == '(':
            answer[i] += 1
print(answer)
