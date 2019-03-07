List = list(map(int, input().split()))

L = List[0]
N = List[1]

numbers = List[2:]

a = 0
answer = 0
for i in range(len(numbers)):
    if numbers[i] - numbers[a] > 2 * L:
        a = i
        answer += 1
answer += 1
print(answer)
