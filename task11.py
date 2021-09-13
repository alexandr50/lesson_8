import random

class LotoCard:
    def __init__(self, type_player):
        self.type_player = type_player
        self._card = [[], [], []]
        self._MAX_NUMBER = 90
        self._COUNT_NUMBER = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self.numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._COUNT_NUMBER)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self.numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)
        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
        return  False

    def try_stroke_number(self, number):
        for index, line in enumerate(self._card):
            for num_index, number_in_card in enumerate(line):
                if number == number_in_card:
                    self._card[index][num_index] = '-'
                    self._numbers_stroked += 1
                    if self._numbers_stroked >= self._COUNT_NUMBER:
                        raise Exception('{} победил!'.format(self.type_player))
                    return True
        return False

    def __str__(self):
        MAX_FIELD_LENGHT = 3
        header = '\n{}:\n-------------------------'.format(self.type_player)
        body = '\n'
        for line in self._card:
            for field in line:
                body += str(field).ljust(MAX_FIELD_LENGHT)
            body += '\n'
        return header + body
class LotoGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self._NUMBERS_COUNT = 90
        MAX_NUMBER = 90
        self.numbers_in_bag = random.sample(range(1, MAX_NUMBER + 1), self._NUMBERS_COUNT)
    def get_number(self):
        return self.numbers_in_bag.pop()

    def start(self):
        for i in range(self._NUMBERS_COUNT):
            print(self._player, self._computer)
            number = self.get_number()
            print('новый боченок {} осталось {}'.format(number, len(self.numbers_in_bag)))
            choice = input('Хотите зачеркнуть? y/n:\n')
            if choice == 'y':
                if not self._player.try_stroke_number(number):
                    print('Игрок проиграл')
                    break
            elif self._player.has_number(number):
                print('Игрок проиграл')
                break
            if self._computer.has_number(number):
                self._computer.try_stroke_number(number)

human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

game = LotoGame(human_player, computer_player)
game.start()












