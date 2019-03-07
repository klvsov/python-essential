a = input().split()
n = a[0]
l = a[1:]
s = list(map(int, l))
s.sort()
answer = 0
for i in range(0, len(s), 2):
    answer += abs(s[i] - s[i+1])
    
print(answer)