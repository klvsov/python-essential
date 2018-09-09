sum = 0
sum_squares = 0
x = int(input())
i = 0
while x != 0:
    i += 1
    sum += x
    sum_squares += x ** 2
    x = int(input())
average = sum ** 2 / i
print(((sum_squares - average) / (i - 1)) ** 0.5)
