h = int(input('Скільки годин пройшло з початку доби? '))

clock_hours = (h // 60) % 24
clock_minutes = h % 60

print(clock_hours, clock_minutes)
