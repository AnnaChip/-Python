# пункт 4:
data = input('Введите несколько слов через пробел: ')
data = data.split(' ')
for ind, el in enumerate(data, 1):
    print(ind, el[:10])
