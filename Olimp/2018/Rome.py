def getRomeNumber(n):
    dn = []
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
    res = dn[0]
    for i in range(1, len(dn)):
        if dn[i] > dn[i-1]:
            a = dn[i] - dn[i-1]
            res -= dn[i - 1]
            res += a
        else:
            res += dn[i]
    return res
a = input()
b = input()
x = getRomeNumber(a)
y = getRomeNumber(b)
print(x+y)