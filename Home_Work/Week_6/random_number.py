import random
true_number = random.randint(0,100)
print(true_number)
while True:
    enter_number = input('Введіть число від 1 до 100: ')
    if enter_number == '' or enter_number == 'exit':
        print('Вихід з програми')
        break
    if not enter_number.isdigit():
        print('Введіть правильне число!')
        continue
    enter_int_number = int(enter_number)
    if true_number == enter_int_number:
        print('Перемога!!!')
        break
    elif true_number < enter_int_number:
        print('Задумане число менше')
    else:
        print('Задумане число більше')
