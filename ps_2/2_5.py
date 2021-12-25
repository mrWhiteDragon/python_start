my_list = [7, 5, 3, 3, 2]
el = int(input('Ввидите новый элемент рейтинга: '))
my_list.append(el)
my_list.sort()
print(sorted(my_list, reverse=True))
