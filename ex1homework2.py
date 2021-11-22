# пункт 2:
time = int(input('введите количество секунд '))
if time < 3600:
    hour = time // 3600
    mnt = time // 60
    sec = time % 60
    print(f'прошло времени: {hour:02}:{mnt:02}:{sec:02}')
else:
    hour = time // 3600
    mnt = (time - 3600 * hour) // 60
    sec = time % 60
    print(f'прошло времени: {hour:02}:{mnt:02}:{sec:02}')
