from random import randint
list = [randint(1, 9) for _ in range(20)]
result = [el for el in list if list.count(el) == 1]
print(list)
print(result)