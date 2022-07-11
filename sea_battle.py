import random


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._x, self._y = x, y
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    @property
    def width(self):
        return self._x + self._length if self._tp == 1 else self._x + 1

    @property
    def height(self):
        return self._y + 1 if self._tp == 1 else self._y + self._length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return (self._x, self._y)

    def move(self, go):
        self._is_move = True if all([x == 1 for x in self._cells]) else False
        if self._is_move:
            if self._tp == 1:
                self.set_start_coords(self._x + go, self._y)
            else:
                self.set_start_coords(self._x, self._y + go)

    def is_collide(self, other):
        return self._y <= other.height and self.height >= other._y and self.width >= other._x and self._x <= other.width

    def is_out_pole(self, size):
        return self.width > size or self.height > size

    def __setitem__(self, key, value):
        self._cells[key] = value

    def __getitem__(self, item):
        return self._cells[item]


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self.pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
    def init(self):
        self.pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        n = 5
        for i in range(4, 0, -1):
            for j in range(1, n - i + 1):
                tp = random.randint(1, 2)
                ship = Ship(i, tp)
                self.set_ship(ship)
                self._ships.append(ship)

    def set_ship(self, ship):
        is_not_set = True
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while (is_not_set):
            ship.set_start_coords(x, y)
            if len(self._ships) == 0 and not ship.is_out_pole(self._size):
                is_not_set = False
            elif all([ship.is_collide(x) == False for x in self._ships]) and not ship.is_out_pole(self._size):
                is_not_set = False
            x = random.randint(0, 9)
            y = random.randint(0, 9)

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            go = random.randint(1, 2)
            temp_coord = ship.get_start_coords()
            ship.move(go)
            if not all([ship.is_collide(x) == False for x in self._ships if
                        x != ship]) or ship.is_out_pole(self._size):
                ship.set_start_coords(temp_coord[0], temp_coord[1])
                go = 3 - go
                ship.move(go)
                if not all([ship.is_collide(x) == False for x in self._ships if x != ship]) or ship.is_out_pole(
                        self._size):
                    ship.set_start_coords(temp_coord[0], temp_coord[1])

    def show(self):
        self.pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            if ship._tp == 1:
                for i in range(ship._x, ship.width):
                    self.pole[i][ship._y] = 1
            else:
                for i in range(ship._y, ship.height):
                    self.pole[ship._x][i] = 1
        for i in range(self._size):
            for j in range(self._size):
                print(self.pole[i][j], end="")
            print()

    def get_pole(self):
        n = len(self.pole)
        return tuple(tuple(self.pole[i][j] for i in range(n)) for j in range(n))

SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()
print(pole.get_pole())
