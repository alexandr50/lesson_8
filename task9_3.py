class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': int(wage), 'bonus': int(bonus)}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income['wage'] + self.income['bonus']

s = Position('alex', 'alex','rr', '1000', '250')
print(s.get_full_name())
print(s.get_total_income())
