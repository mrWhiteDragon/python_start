def sum_func():
    sum = 0
    while True:
        num_list = input('Введите несколько чисел через пробел или Q для завершения: ').split()
        for num in num_list:
            if num == 'q' or 'Q':
                return sum
            else:
                try:
                    sum += int(num)
                except ValueError:
                    print('Ошибка. Требуются числа')
        print('Сумма чисел - ', sum)

print(sum_func())