S = input()
a = S.find('h')
b = S.rfind('h')-1
y = S[b:a:-1]
print(S[:S.find('h')+1] + y + S[S.rfind('h'):])
