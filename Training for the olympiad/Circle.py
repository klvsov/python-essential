M = int(input())

i = 0

count = 0


while i <= M:
    if count % 2 != 0:
        i += 20

    if count %2 == 0:
        i += 10
    count += 1

print(count-1)
