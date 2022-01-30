from itertools import cycle, count

for n in count(3):
    print(n)
    if n == 10:
        break

print('\n')

list = ['A', 'B', 'C']
count = 0
for i in cycle(list):
    if count == 9:
        break
    print(i)
    count += 1