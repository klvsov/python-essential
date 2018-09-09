p = int(input('Відсотки вкладу - '))
x = int(input('Сума вкладу, гривень - '))
y = int(input('Сума вкладу, копійок - '))

all_start_sum = x * 100 + y

all_end_sum = all_start_sum * (p / 100) + all_start_sum

print(int(all_end_sum // 100), int(all_end_sum % 100))
