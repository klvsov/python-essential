from time import *
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
start = time()
#print(f(int(input())))
fib(int(input()))
print(time() - start)