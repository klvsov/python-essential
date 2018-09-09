import math

r1 = float((input('Введіть довжину першого кола - ')))

r2 = r1 * 2

s = math.pi * r2 ** 2
l = 2 * math.pi * r2

print('Довжина другого кола -', l, 'Площа другого круга -', s)
