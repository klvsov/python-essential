# f = 1
# s = 1
# i = 2
# n = int(input())
# while i < n:
#     sum = f + s
#     f = s
#     s = sum
#     i += 1
# print(sum)


f = 1
s = 1
n = int(input())
for i in range(2, n):
     sum = f + s
     f = s
     s = sum
print(sum)
