class Car:
    def __init__(self, color, name, is_police, speed=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed += 20
        print(f'Машина разгонятеся, скорость увеличена на 20 км/ч')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn_left(self):
        print('Машина повернула налево')

    def turn_right(self):
        print('Машина повернула направо')

    def show_speed(self):
        print(f'Скорость авто {self.speed} км/ч')


class TownCar(Car):
    speedlimit = 60

    def show_speed(self):
        if self.speed > self.speedlimit:
            print(f'Скорость авто {self.speed} км/ч, превышение скорости!!!')
        else:
            print(f'Скорость авто {self.speed} км/ч')


class SportCar(Car):
    speedlimit = None


class WorkCar(Car):
    speedlimit = 40

    def show_speed(self):
        if self.speed > self.speedlimit:
            print(f'Скорость авто {self.speed} км/ч, превышение скорости!!!')
        else:
            print(f'Скорость авто {self.speed} км/ч')


class PoliceCar(Car):
    speedlimit = None


mycar = WorkCar('red', 'FIAT', False)
print(mycar.is_police)
mycar.turn_left()
mycar.go()
mycar.go()
mycar.go()
mycar.show_speed()
mycar.stop()
mycar.show_speed()