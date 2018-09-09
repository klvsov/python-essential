S = input()
print(S[:S.find('h')+1])
print(S[S.find('h')+1:S.rfind('h'):-1])
print(S[:S.rfind('h')-1])

