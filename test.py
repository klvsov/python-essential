el = input().split()

for i in range(len(el)):
     el[i] = int(el[i])

for i in range(1, len(el)):
    if el[i] > el[i-1]:
         print(el[i])
