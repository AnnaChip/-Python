# пункт 5:
my_list = [7, 5, 3, 3, 2]
number = int(input("введите натуральное число: "))
ind = 0
for n in my_list:
    if number <= n:
        ind += 1
    elif number > n:
           break
my_list.insert(ind, number)
print(my_list)
