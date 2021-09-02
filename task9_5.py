class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'start drawing'

class Pen(Stationery):
    def draw(self):
        return f'start drawing {self.title}'
class Pencil(Stationery):
    def draw(self):
        return f'start drawing {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'start drawing {self.title}'
p = Pen('pen')
print(p.draw())
s = Pencil('pencil')
print(s.draw())
h = Handle('handle')
print(h.draw())