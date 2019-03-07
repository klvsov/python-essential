N = input().split()
n = int(N[0])
N.remove(str(n))
A = []
for i in range(len(N)):
    A.append(N[i])
A.sort()

A = list(map(int, A))
Max = max(A)
num_col = 1
count = 0
ans = []
while num_col < Max:
    for i in range(len(A)):
        if A[i] > num_col:
            count += 1
    ans.append(count)
    count = 0
    num_col += 1
A.append(n)
A += ans
for i in range(len(A)):
    print(A[i], end=' ')