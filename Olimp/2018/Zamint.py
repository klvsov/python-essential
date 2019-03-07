N = input().split()
L = int(N[0])
n = N[2:]

for i in range(len(n)):
    n[i] = int(n[i])
n.sort()
last = 0
x = len(n)
for i in range(1, len(n)):
    if abs(n[last] - n[i]) == 2 * L:
        x -= 1
    if abs(n[last] - n[i]) == L:
        x -= 1
    if abs(n[last] - n[i]) == 0:
        x -= 1
    last += 1
print(x)