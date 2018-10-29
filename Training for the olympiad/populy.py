import math
m = int(input())
n = int(input())
lst = [2]

for i in range(3, n+1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j > int((math.sqrt(i)) + 1):
            lst.append(i)
            break
        if i % j == 0:
            break
    else:
        lst.append(i)

my_str = ''.join(map(str, lst))
#print(my_str.count('1'))

ls = []
for i in range(1, 10):
    max = my_str.count(str(i))
    ls.append(max)
    break
print(i)
