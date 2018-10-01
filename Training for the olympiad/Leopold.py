N,L,K = (input()).split()

N = int(N)
L = int(L)
K = int(K)

count = 1
All = 0

while count <= N:
    All += L
    L += K
    count += 1

print(All)
