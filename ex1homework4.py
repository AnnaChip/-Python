# пункт 4:
n = int(input("Введите целое положительное число "))
maxn = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > maxn:
        maxn = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", maxn)
    break