# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран
with open('new_5.txt', 'w', encoding='utf-8') as f:
   f.write('10 10 10 10')

with open('new_5.txt', 'r', encoding='utf-8') as f:
   data = f.read()
   result = [int(el) for el in data.split()]
   print(sum(result))
