k = int(input())
n = int(input())

ls = []
while n > 0:
    n, a = divmod(n, k)
    ls = [str(a)] + ls


print(''.join(ls))

