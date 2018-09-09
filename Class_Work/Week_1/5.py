class_1 = int(input('Кількість учнів в А класі '))
class_2 = int(input('Кількість учнів в Б класі '))
class_3 = int(input('Кількість учнів в В класі '))

all_class = class_1 // 2 + class_1 % 2 + class_2 // 2 + class_2 % 2 + class_3 // 2 + class_3 % 2

print('Всього потрібно', all_class, 'парт(и)')
