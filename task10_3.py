class Cell:
    def __init__(self, nums):
        self.nums = nums
    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) \
               + '\n ' + '*' * (self.nums % rows)
    def __add__(self, other):
        return 'сумма клеток: ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'яйчеек в первой клетке меньше чем во второй'
    def __mul__(self, other):
        return 'умножение клеток равно: ' + self.nums * other.nums
    def __truediv__(self, other):
        return 'деление клеток равно: ' + str(round(self.nums / other.nums))

cell_1 = Cell(55)
cell_2 = Cell(44)
print(cell_1 - cell_2)
print(cell_2.make_order(10))