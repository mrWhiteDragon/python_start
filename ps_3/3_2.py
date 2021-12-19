# 1 способ
def data_to_str(*args):
    return print(f'{name} {surname} {year} {city} {email} {phone}')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

data_to_str(name, surname, year, city, email, phone)

# 2 способ
# def data_to_str(**kwargs):
#     return print(' '.join(kwargs.values()))
#
# data = {
#     'name': input('Введите имя: '),
#     'surnsme': input('Введите фамилию: '),
#     'year': input('Введите года рождения: '),
#     'city': input('Введите город: '),
#     'email': input('Введите email: '),
#     'phone': input('Введите телефон: '),
# }
#
# data_to_str(**data)
