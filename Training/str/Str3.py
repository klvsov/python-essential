S = input()
a = int(len(S)//2) + len(S) % 2
print(S[a:]+S[:a])
