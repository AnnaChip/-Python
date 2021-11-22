# пункт 6:
a = int(input('Введите сколько км спортсмен пробежал за первый день: '))
b = int(input('Введите  сколько км должен пробежать спортсмен: '))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете результатов на %.d день" % result_days)
