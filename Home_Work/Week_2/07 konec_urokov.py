nl = int(input())
length = nl * 45 + (nl // 2) * 5 + ((nl + 1) // 2 - 1) * 15
print(length // 60 + 9, length % 60)
