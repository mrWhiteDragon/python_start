def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False


words = input('Введте строку из слов, разделеных пробелами: ').split()
for w in words:
    res = int_func(w)
    if res:
        print(int_func(w), ' ')
