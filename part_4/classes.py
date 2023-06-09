import math
from functools import singledispatchmethod

from part_2.quantify import iterable


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


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)


class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if not (isinstance(hours, int) and 1 <= hours <= 12):
            raise ValueError("Некорректное время")
        self._hours = hours

    hours = property(get_hours, set_hours)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()


def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10**9


class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError("Изменение логина невозможно")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hash_function(password)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return Rectangle(side, side)


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @classmethod
#     def from_diameter(cls, diameter):
#         return Circle(diameter / 2)


class Pet:

    all_pets = []

    def __init__(self, name):
        self.name = name
        self.all_pets.append(self)

    @classmethod
    def first_pet(cls):
        # Ради интереса попрактиковался с match-case.
        match cls.all_pets:
            case []:
                return None
            case [first_pet, *_]:
                return first_pet

    @classmethod
    def last_pet(cls):
        match cls.all_pets:
            case []:
                return None
            case [*_, last_pet]:
                return last_pet

    @classmethod
    def num_of_pets(cls):
        return len(cls.all_pets)


class StrExtension:
    @staticmethod
    def remove_vowels(string: str):
        return "".join(x for x in string if x.lower() not in "aeyiou")

    @staticmethod
    def leave_alpha(string: str):
        return "".join(x for x in string if x.isalpha())

    @staticmethod
    def replace_all(string: str, chars: list, char: str):
        return "".join(x if x not in chars else char for x in string)


# pet1 = Pet("Ratchet")
# pet2 = Pet("Clank")
# pet3 = Pet("Rivet")
#
# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())


class Processor:
    @singledispatchmethod
    def process(self, data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @staticmethod
    @process.register(int)
    @process.register(float)
    def _from_int_float_process(data):
        return data * 2

    @staticmethod
    @process.register(str)
    def _from_str_process(data):
        return data.upper()

    @staticmethod
    @process.register(list)
    def _from_list_process(data):
        return sorted(data)

    @staticmethod
    @process.register(tuple)
    def _from_tuple_process(data):
        return tuple(sorted(data))


# print(
#     StrExtension.remove_vowels(
#         "Success is the ability to go from failure to failure without losing your enthusiasm."
#     )
# )
# print(
#     StrExtension.remove_vowels(
#         "Success is the ability to go from failure to failure without losing your enthusiasm.".upper()
#     )
# )


# from functools import singledispatchmethod
#
#
# class MyClass:
#     @singledispatchmethod
#     def base_implementation(self, arg):
#         print("Базовая реализация")
#
#     @base_implementation.register
#     def intfloat_implementation(self, arg: int | float):
#         print(type(arg))
#         print("Реализация для целочисленного и вещественного аргументов")
#
#
# obj = MyClass()
#
# obj.base_implementation(1)
# obj.base_implementation(1.0)


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @staticmethod
    @neg.register(float)
    @neg.register(int)
    def _from_float_int_neg(data: float | int):
        return -data

    @staticmethod
    @neg.register(bool)
    def _from_bool_neg(data: bool):
        return not data


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @staticmethod
    @format.register(int)
    def _(data):
        print(f"Целое число: {str(data)}")

    @staticmethod
    @format.register(float)
    def _(data):
        print(f"Вещественное число: {str(data)}")

    @staticmethod
    @format.register(list)
    def _(data):
        print(f"Элементы списка: {', '.join(str(x) for x in data)}")

    @staticmethod
    @format.register(tuple)
    def _(data):
        print(f"Элементы кортежа: {', '.join(str(x) for x in data)}")

    @staticmethod
    @format.register(dict)
    def _(data):
        data_to_print = [(k, v) for k, v in data.items()]
        print(f"Пары словаря: {str(data_to_print).strip('[]')}")


Formatter.format({"Cuphead": 1, "Mugman": 3})


# Formatter.format([10, 20, 30, 40, 50])
# Formatter.format(([1, 3], [2, 4, 6]))
Formatter.format({1: "one", 2: "two"})
Formatter.format({1: True, 0: False})


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def discriminant(self):
        return self.b * self.b - 4 * self.a * self.c

    @property
    def x1(self):
        discriminant = self.discriminant
        if discriminant < 0:
            return None
        return (-self.b - discriminant**0.5) / (2 * self.a)

    @property
    def x2(self):
        discriminant = self.discriminant
        if discriminant < 0:
            return None
        return (-self.b + discriminant**0.5) / (2 * self.a)

    @property
    def view(self):
        # Передаю спасибо линтеру Black за то, что помог мне отформатировать этот ужас.
        view_string = (
            f"{self.a}x^2 "
            f"{'-' if self.b < 0 else '+'} {abs(self.b)}x "
            f"{'-' if self.c < 0 else '+'} {abs(self.c)}"
        )

        return view_string

    @property
    def coefficients(self):
        return f"({self.a}, {self.b}, {self.c})"

    @coefficients.setter
    def coefficients(self, coefficients):
        self.a, self.b, self.c = coefficients

    @classmethod
    def from_iterable(cls, coefficients: iterable):
        return QuadraticPolynomial(*coefficients)

    @classmethod
    def from_str(cls, coefficients: str):
        return QuadraticPolynomial(*[float(x) for x in coefficients.split()])
