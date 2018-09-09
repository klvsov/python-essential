import math

x = float(input())

a, b = math.modf(x)

print(math.trunc(a * 10))
