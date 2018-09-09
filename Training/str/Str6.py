S = input()
c = S.count('f')
num = 0
if c == 1:
    print(-1)
elif c == 0:
    print(-2)
else:
    print(S.find('f', S.find('f') + 1))
