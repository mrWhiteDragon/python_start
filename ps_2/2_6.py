fields = ['название', 'цена', 'количество', 'ед']
i = 1
goods = []

# Вводим данные товаров:
print('\nВведите через пробел характеристики товара.\n'
      'Например: \nКомпьютер 20000 5 шт.\n'
      'Для завершения нажмите Enter.\n')
while True:
    data = input('>>>')
    if data == '':
        break
    data = list(data.split())
    if len(data) != len(fields) :
        print('Ошибка')
        continue

# Укладываем данные товаров в список кортежей и словарей:
    d = {}
    n = 0
    while n < len(data):
        for field in fields:
            d[field] = data[n]
            n += 1

    data = (i, d)
    i += 1
    goods.append(data)

    print(data)

# Выводим весь список товаров:
print('\nСписок товаров:')
for good in goods:
    print(good)

# Формируем и выводим словарь аналитики:
analitic_dict = {}
for field in fields:
    a = []
    for good in goods:
        a.append(good[1][field])
    analitic_dict[field] = a

print(f'\nСловарь аналитики:\n{analitic_dict}')
