# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

data = [1, 2, 5, 46, 4, 9, 1, 12]

new_data = [int(el) for el in data]
for i in range(1, len(new_data)):
    if new_data[i] > new_data[i - 1]:
        print(new_data[i])

# или:

new_data_2 = [data[el] for el in range(1, len(data)) if data[el] > data[el - 1]]
print(new_data_2)
