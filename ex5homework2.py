# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
my_str = 0
my_words = 0
f = open('new_2', 'r')
for line in f:
    my_str += 1
    word = line.split()
    my_words = len(word)
    print(f'номер строки: {my_str}')
    print(f'количество слов в строке: {my_words}')
f.close()
print(f'общее количество строк: {my_str}')





