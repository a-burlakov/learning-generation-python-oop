class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.program_name = "GenerationPy"
        self.environment = "release"
        self.loglevel = "verbose"
        self.version = "1.0.0"


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"


class IPAddress:
    def __init__(self, ip):
        if isinstance(ip, str):
            self.ip = tuple(ip.split("."))
        elif isinstance(ip, list) or isinstance(ip, tuple):
            self.ip = tuple(ip)

    def __repr__(self):
        return f"IPAddress('{'.'.join(str(n) for n in self.ip)}')"

    def __str__(self):
        return ".".join(str(n) for n in self.ip)


class PhoneNumber:
    def __init__(self, phone_number: str):
        self.number = phone_number.replace(" ", "")

    def __str__(self):
        return f"({self.number[:3]}) {self.number[3:6]}-{self.number[6:10]}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.number}')"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"Вектор на плоскости с координатами ({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return len(other) == 2 and self.x == other[0] and self.y == other[1]
        return NotImplemented


from dataclasses import dataclass
from functools import total_ordering


@dataclass
@total_ordering
class Word:
    word: str

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.word}')"

    def __str__(self):
        return self.word.capitalize()

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Word):
            return len(self.word) > len(other.word)
        return NotImplemented


print(Word("bee") == Word("hey"))
print(Word("bee") < Word("geek"))
print(Word("bee") > Word("geek"))
print(Word("bee") <= Word("geek"))
print(Word("bee") >= Word("gee"))
