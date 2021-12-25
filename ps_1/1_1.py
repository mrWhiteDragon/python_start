name = 'Иван'
surname = 'Петров'
age = 33
height = 180
weight = 80

print(f'Образец резюме:\n Имя: {name}\n Фамилия: {surname}\n '
      f'Возраст: {age}\n Рост: {height}\n Вес: {weight}\n')

user_name = input('Введите ваше имя: ')
user_surname = input('Введите вашу фамилию: ')
user_age = input('Введите ваш возраст: ')
user_height = input('Введите ваш рост: ')
user_weight = input('Введите ваш вес: ')

name = user_name
surname = user_surname
age = user_age
height = user_height
weight = user_weight

print(f'\n Спасибо!\n\n Вот ваше резюме:\n Имя: {name}\n Фамилия: {surname}\n '
      f'Возраст: {age}\n Рост: {height}\n Вес: {weight}')
