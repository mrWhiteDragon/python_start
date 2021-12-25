# 1 способ
def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >=0:
            print('Ошибка. x должен быть больше нуля, а y меньше')
        else:
            return print(f'{x} ** {y} = {round(x ** y, 6)}')
    except ValueError:
        return print('Программа работает только с числами')

# 2 способ
# def my_func(x, y):
#     try:
#         x, y = float(x), int(y)
#         if x <= 0 or y >=0:
#             print('Ошибка. x должен быть больше нуля, а y меньше')
#         else:
#             res = x
#             for n in range(abs(y)):
#                 res = res / x
#             return print(f'{x} ** {y} = {round(res, 6)}')
#     except ValueError:
#         return print('Программа работает только с числами')

my_func(5, -3)