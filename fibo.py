n = int(input())
first = 1
second = 1

for i in range(2, n):
    sum = first + second
    first = second
    second = sum
print(sum)
