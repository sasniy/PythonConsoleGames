import random


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.init()

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    @classmethod
    def check_indx(cls, indx1, indx2):
        if not isinstance((indx1 or indx2), int) or (indx1 or indx2) not in range(0, 3):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        indx1, indx2 = item
        self.check_indx(indx1, indx2)
        return self.pole[indx1][indx2].value

    def __setitem__(self, key, value):
        indx1, indx2 = key
        self.check_indx(indx1, indx2)
        if value in (self.COMPUTER_O, self.HUMAN_X):
            self.pole[indx1][indx2].value = value

    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.pole[i][j].value, end="")
            print()

    def human_go(self):
        indx1, indx2 =map(int,input("Введите координаты свободной клетки:").split())
        self[indx1, indx2] = self.HUMAN_X

    def computer_go(self):
        temp = tuple(filter(lambda x:x,self.pole))
        random.choice(random.choice(temp)).value = self.
        value = random.choice(random.choice(self.pole))
        while not value:
            value = random.choice(random.choice(self.pole))
        value.value = self.COMPUTER_O

    def check_win(self, value):
        return any([all([self.pole[i][j].value == value for i in range(3)]) for j in range(3)]) \
               or any([all([self.pole[j][i].value == value for i in range(3)]) for j in range(3)]) \
               or all([self.pole[i][i].value == value for i in range(3)]) \
               or all([self.pole[i][2 - i].value == value for i in range(3)])

    def check_draw(self):
        return all([all([self.pole[i][j].value != self.FREE_CELL for i in range(3)]) for j in range(3)])

    @property
    def is_draw(self):
        return self.check_draw()

    @property
    def is_human_win(self):
        return self.check_win(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.check_win(self.COMPUTER_O)

    def __bool__(self):
        return not self.is_draw and not self.is_computer_win and not self.is_human_win


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()
    print('----')
    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
