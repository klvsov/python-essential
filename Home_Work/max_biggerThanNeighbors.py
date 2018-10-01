m = input().split()
n = 0
for i in range(0, len(m)):
    m[i] = int(m[i])
for i in range(1, len(m)-1):
    if m[i] > m[i]-1 and m[i] < m[i]+1:
        n += 1
