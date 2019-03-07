N, a, b, c = input().split()
N = int(N)
a = int(a)
b = int(b)
c = int(c)

min_m = min(a, b, c)
max_m = max(a, b, c)
A = [a, b, c]
A.remove(min_m)
A.remove(max_m)
middle_m = A[0] 


count = 0
while N != 0:
    if N >= min_m:
        N -= min_m
        count += 1
    elif N < 2 * min_m and N >= middle_m:
        N -= middle_m
        count += 1
    elif N < 2 * middle_m and N >= max_m:
        N -= max_m
        count += 1

print(count)