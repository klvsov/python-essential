N, L, K = input().split()
N = int(N)
L = int(L)
K = int(K)
s = 0
c = 1
while N >= c:
    s += L
    L += K
    c += 1
print(s)
