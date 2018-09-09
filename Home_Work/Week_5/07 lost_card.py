n = int(input())
sum_card, sum_all_card = 0, 0
for i in range(1, n):
    sum_card += int(input())
for j in range(1, n + 1):
    sum_all_card += j
lost_card = sum_all_card - sum_card
print(lost_card)
