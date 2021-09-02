class Road:
    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht
        self.weight = 50
        self.high = 6
    def calculate_mass(self):
        calculate_mass = self._lenght * self._widht * self.weight * self.high / 1000
        print(f'Для покрытия дорожного полотна полностью потребуется: {round(calculate_mass)} тонн асфальта')
r = Road(1000, 6)
r.calculate_mass()
