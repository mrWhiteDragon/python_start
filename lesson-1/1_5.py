proceeds = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))

if proceeds > costs:
    profit = proceeds - costs
    profitability = int((profit / proceeds) * 100)
    print('Поздравляю! Фирма работает с прибылью. \n'
          f'Рентабильность составляет: {profitability} %\n')

    employees = int(input('Введите численность сотрудников фирмы: '))
    profit_per_employee = profit / employees

    print(f'Прибыль на одного сотрудника составляет: {profit_per_employee}')
else:
    print('К сожалению фирма работает с убытком.')

