# 1 способ без аргументов
# def salary_count(hours, pay_per_hour, premium):
#     salary = (hours * pay_per_hour) + premium
#     return print(salary)
#
# salary_count(192, 500, 5000)

# 2 способ с аргументами
from sys import argv
def salary_count():
    try:
        hours, pay_per_hour, premium = map(float, argv[1:])
        print(f'Зарплата - {(hours * pay_per_hour) + premium}')
    except ValueError:
        print('Введите 3 числа. Не строки и не пустой ввод')

salary_count()