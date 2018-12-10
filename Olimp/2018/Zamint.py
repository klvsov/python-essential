n = []
N = input()
n.append(N)
for i in range(len(n)):
    if n[i] == n[i-1]:
        print(1)
    else:
        print(0)