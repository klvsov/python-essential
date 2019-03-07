n, k = input().split()
n = int(n)
k = int(k)

answer = False

lst = []
for i in range(n):
    lst.append(input())
for i in range(len(lst)):
    if lst.count(lst[i]) == n - k:
        answer = lst[i]

if answer and n - k != 1:
    print(answer)
else:
    print(-1)
