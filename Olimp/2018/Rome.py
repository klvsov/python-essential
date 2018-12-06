n = input()

dn = []
res = 0
for i in range(len(n)):
    if n[i] == 'I':
        dn.append(1)
    elif n[i] == 'V':
        dn.append(5)
    elif n[i] == 'X':
        dn.append(10)
    elif n[i] == 'L':
        dn.append(50)
    elif n[i] == 'C':
        dn.append(100)
    elif n[i] == 'D':
        dn.append(500)
    elif n[i] == 'M':
        dn.append(1000)
for i in range(len(dn)):
    if dn[i] < dn[i-1]:
        a = dn[i-1] - dn[i]
        res += a
        res -= dn[i - 1]
    else:
        res += dn[i]
    print(dn[i],end=" ")
    print(dn[i-1])
    print(res)