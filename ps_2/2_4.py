user_string = list(input('Введите строку из нескольких строк, разделенных пробелами: ').split())
n = 1
for word in user_string:
    print(f'{n}. {word[:10]}')
    n += 1