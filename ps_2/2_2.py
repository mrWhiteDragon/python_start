print('Заполни список. Для завершения нажми \'Enter\'.')
list = []
while True:
    a = input('Введи элемент списка: ')
    if a == '':
        break
    list.append(a)

for i in range(1, len(list), 2):
    list[i - 1], list[i] = list[i], list[i - 1]
print(list)

# 2 способ:
# list = list(input('Введите элементы списка, разделенные пробелом: ').split())
#
# for i in range(1, len(list), 2):
#     list.insert(i - 1, list.pop(i))
# print(list)




