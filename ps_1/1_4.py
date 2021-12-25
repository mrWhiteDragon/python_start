number = int(input('Введите целое число: '))
n_max = number % 10
num = number

while num > 0:
    n = num % 10
    if n > n_max:
        n_max = n

    if n == 9:
        break

    num //= 10
    print(num)

print(f'Наибольшая цифра в числе {number} равна {n_max}')