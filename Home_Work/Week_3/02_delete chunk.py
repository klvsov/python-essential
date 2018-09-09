S = input()
print(S[:S.find('h')]+S[S.rfind('h')+1:])
