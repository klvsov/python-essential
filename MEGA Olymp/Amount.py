number = int(input())
if number < 11 or number == 12:
	print(0, 0, 0, 0)
elif number == 13:
	print(2, 3, 7, 1)
elif number == 15:
	print(2, 5, 7, 1)
else:
	print(2, 3, 5, number - 10)