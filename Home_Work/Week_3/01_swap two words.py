S = input()
space = S.find(' ')
print(S[space+1:] + ' ' + S[:space])
