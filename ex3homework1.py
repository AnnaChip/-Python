# пункт 1:
def my_division(a, b):
    return a / b


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число, не равное нулю: '))
if num_2 == 0:
    print('Ошибка! делить на ноль нельзя')
else:
    print(my_division(num_1, num_2))
