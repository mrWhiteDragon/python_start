import sys
def my_func(*args):
        args = sorted(list(args))
        return print(f'Сумма наибольших двух аргументов {args[-1]} и {args[-2]} равна {args[-1]+args[-2]}')

def input_and_validate():
    try:
        num_1 = int(input('Ввведите 1-е число: '))
        num_2 = int(input('Ввведите 2-е число: '))
        num_3 = int(input('Ввведите 3-е число: '))
        return num_1, num_2, num_3
    except ValueError:
        print('Можно вводить только числа' )
        sys.exit()

arg_1, arg_2, arg_3 = input_and_validate()
my_func(arg_1, arg_2, arg_3)

