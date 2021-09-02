import itertools
from itertools import cycle
from time import sleep
class TrafficLight:
    def __init__(self,):
        self.__color = (('red', 7), ('yellow', 2), ('green', 5))

    def running(self):
        for color, second in cycle(self.__color):
            print(color, second)
            sleep(second)

t = TrafficLight()
t.running()