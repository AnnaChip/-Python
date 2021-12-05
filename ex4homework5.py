# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные
# числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

data = []
for el in range(100, 1001, 2):
    data.append(el)

result = 1
for el in data:
    result = result * el
print(result)

# или так:
from functools import reduce

def my_func(a, b):
    return a * b

print(reduce(my_func, data))

# генератором:

print(reduce(lambda a, b: a * b, [el for el in range(100, 1001, 2)]))



