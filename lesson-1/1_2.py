time = int(input('Введите количество секунд: '))

hours = int(time / 3600)
minuts = int((time % 3600) / 60)
seconds = int((time % 3600) % 60)

print(f'Время: {hours:02d}:{minuts:02d}:{seconds:02d}')

# 2 способ:
# import datetime
# s = int(input('Введите количество секунд: '))
# time = datetime.timedelta(seconds = s)
# print(f'Время: {time}')


