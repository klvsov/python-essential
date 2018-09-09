S = input()

c = S.count('f')

if c == 1:
    print(S.find('f'))
elif c >= 2:
    print(S.find('f'), S.rfind('f'))
