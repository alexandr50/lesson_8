from random import randint
field = []
for row in range(1, 11):
    row = []
    for i in range(1, 11):
        row.append(' 0')
    field.append(row)

def print_field(field):
     print('    A  B  C  D  E  F  G  H  I  G')
     for num, col in enumerate(field, 1):
         print('% -2d' % num, *col)  # создаю игровое поле

def random_row(field):
    return randint(0, len(field) - 1)  # ф-я загадывания коробля по строке

def random_col(field):
    return randint(0, len(field) - 1)  # ф-я загадывания коробля по столбцу

print_field(field)
ship_row = random_row(field)
ship_col = random_col(field)
running = True
while running:
    print(ship_row, ship_col)
    guess_col = int(input('Введите номер столбца: '))
    guess_row = int(input('Введите номер строки: '))
    if guess_col == ship_col and guess_row == ship_row:
        print('Вы попали, конец игры')
        running = False
    else:
        if (guess_col < 0 or guess_col > 10) or (guess_row < 0 or guess_row > 10):
            print('Вы стреляете мимо поля')
        elif field[guess_col][guess_row] == 'X':
            print('Вы уже стреляли в эту точку')
        else:
            field[guess_col][guess_row] = 'X'
    print_field(field)






