from functools import reduce
list = [el for el in range(100, 1001) if el % 2 == 0 ]
print('Список: ', list)

def func(a, b):
    return a * b

print('Произведение всех элементов списка: ', reduce(func, list))
