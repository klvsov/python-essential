number = int(input('Введіть трицифрове число '))
# 123
number1 = number // 100
number2 = number % 100 // 10
number3 = number % 10

print(number1, number2, number3, sep='\n')
