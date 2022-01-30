def division(a, b):
    '''Делит a на b'''
    try:
        a, b = int(a), int(b)
        result = a / b
    except ValueError:
        return print('Некорректные данные')
    except ZeroDivisionError:
        return print('На ноль делить нельзя')
    return print(f'{a} / {b} = {round(result, 4)}')

print('Деление чисел')
a = input('Введите первое число: ' )
b = input('Введите второе число: ' )

division(a, b)