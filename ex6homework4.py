# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar
# и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Текущая скорость {self.name} составляет {self.speed}. Сбросьте скорость!'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed}. Оптимально!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return print(f'Текущая скорость {self.name} составляет {self.speed}. Сбросьте скорость!')
        else:
            return f'Текущая скорость {self.name} составляет {self.speed}. Оптимально!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

Volvo = Car (150, 'Green', 'Volvo', False)
Lamba = SportCar(100, 'Red', 'Lamba', False)
Lada = TownCar(30, 'White', 'Lada', False)
Kia = TownCar(90, 'White', 'Kia', False)
Cat = WorkCar(70, 'Orange', 'Cat', False)
Niva = PoliceCar(110, 'Blue', 'Niva', True)
print(Lamba.go())
print(Volvo.show_speed())
print(Lada.show_speed())
print(Cat.show_speed())
print(Kia.show_speed())
print(Niva.stop())
print(Cat.turn_left())
