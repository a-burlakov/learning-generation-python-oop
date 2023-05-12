import math


class Gun:
    def __init__(self):
        self.shoot_style = "pif"
        self.next_shoot_style = "paf"
        self.counter = 0

    def shoot(self):
        print(self.shoot_style)
        self.shoot_style, self.next_shoot_style = (
            self.next_shoot_style,
            self.shoot_style,
        )
        self.counter += 1

    def shots_count(self):
        return self.counter

    def shots_reset(self):
        self.counter = 0


#
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.friends = 0
#
#     def add_friends(self, n):
#         self.friends += n


class Numbers:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def get_even(self):
        return [x for x in self.numbers if x % 2 == 0]

    def get_odd(self):
        return [x for x in self.numbers if x % 2 != 0]


class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color

    def add_rooms(self, n):
        self.rooms += n


from math import pi


class Bee:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_left(self, n):
        self.x -= n

    def move_right(self, n):
        self.x += n


class Scales:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, m):
        self.right += m

    def add_left(self, m):
        self.left += m

    def get_result(self):
        if self.left == self.right:
            return "Весы в равновесии"
        elif self.left > self.right:
            return "Левая чаша тяжелее"
        else:
            return "Правая чаша тяжелее"


class Vector:
    def __init__(self):
        self.x = 0
        self.y = 0

    def abs(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))


class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, words: str):
        self.words.extend(words.split())

    def get_shortest_words(self):
        if not self.words:
            return []
        min_len = len(min(self.words, key=len))
        return [w for w in self.words if len(w) == min_len]

    def get_longest_words(self):
        if not self.words:
            return []
        max_len = len(max(self.words, key=len))
        return [w for w in self.words if len(w) == max_len]


class Wordplay:
    def __init__(self, words: list = None):
        if words is None:
            words = []

        self.words = words.copy()

    def add_word(self, word: str):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int):
        return [w for w in self.words if len(w) == n]

    def only(self, *args):
        return [w for w in self.words if all(s in args for s in w)]

    def avoid(self, *args):
        return [w for w in self.words if all(s not in args for s in w)]


from math import pi


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * radius * radius

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


class BankAccount:
    def __init__(self, balance: int | float = 0):
        self._balance: int | float = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount: int | float):
        self._balance += amount

    def withdraw(self, amount: int | float):
        if self._balance < amount:
            raise ValueError("На счете недостаточно средств")
        else:
            self._balance -= amount

    def transfer(self, account: "BankAccount", amount: int | float):
        if self._balance < amount:
            raise ValueError("На счете недостаточно средств")
        else:
            self._balance -= amount
            account.deposit(amount)


class User:
    def __init__(self, name: str, age: int):
        self._name: str = ""
        self._age: int = 0
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, new_name: str):
        if isinstance(new_name, str) and new_name and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("Некорректное имя")

    def get_age(self):
        return self._age

    def set_age(self, new_age: int):
        if isinstance(new_age, int) and new_age and 0 <= new_age <= 110:
            self._age = new_age
        else:
            raise ValueError("Некорректный возраст")
