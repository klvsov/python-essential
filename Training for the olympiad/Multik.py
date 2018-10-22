N, K = input().split()

N = int(N)
K = int(K)
count1 = 0
count2 = 0
for i in range(K, N):
    count1 += 1

for i in range(0, N, 2):
    count2 += 1

if count1 >= count2:
    print(1)
else:
    print(0)
