class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} driving'

    def stop(self):
        return f'{self.name} stoped'

    def turn(self, direction):
        return f'{self.name} turn {direction}'
    def show_speed(self):
        return f'Your speed is {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Your speed is very high'
        else:
            return f'Your speed is normal'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Your speed is very high'
        else:
            return f'Your speed is normal'

class PoliceCar(Car):
    pass
c =Car(60,'red', 'ferarri', False)
print(c.go(), c.show_speed(), c.turn('left'), c.stop())
t = TownCar(80, 'blue', 'volkswagen', False)
print(t.go(), t.show_speed(), t.turn('right'), t.stop())

s = SportCar(100, 'yellow', 'porshe', False)
print(s.go(), s.show_speed(), s.turn('left'), s.stop())

w = WorkCar(40, 'orange', 'kamaz', False)
print(w.go(), w.show_speed(), w.turn('right'), w.stop())

p = PoliceCar(150, 'black', 'skoda', True)
print(p.go(), p.show_speed(), p.turn('right'), p.stop())




