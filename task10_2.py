from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, parametr):
        self.parametr = parametr
    @abstractmethod
    def consumption(self):
        pass



class Coat(Clothes):
    @property
    def consumption(self):
        return f'Потребуется для пошива пальто {round(self.parametr / 6.5 + 0.5)} ткани'


class Costume(Clothes):
    @property
    def consumption(self):
        return f'Потребуется для пошива костюма {round(self.parametr * 2 + 0.3)} ткани'


coat = Coat(50)
print(coat.consumption)
costume = Costume(50)
print(costume.consumption)
