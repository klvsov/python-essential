S = input()
print(S[:S.find('h')+1] + S[S.find('h')+1:S.rfind('h')].replace('h','H') + S[S.rfind('h'):])
