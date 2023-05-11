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


class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n


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


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.area = pi * radius * radius


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


words = ["Лейбниц", "Бэббидж", "Нейман", "Джобс", "да_Винчи", "Касперский"]
wordplay = Wordplay(words)

words.extend(["Гуев", "Харисов", "Светкин"])
print(words)
print(wordplay.words)
