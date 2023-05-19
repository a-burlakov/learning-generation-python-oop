class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)  # список покупок
        self.customer = customer  # имя покупателя

    def __iter__(self):
        return iter(self.cart)


class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    def __iter__(self):
        yield from (
            self.x,
            self.y,
            self.z,
        )


class DevelopmentTeam:
    def __init__(self):
        self._juniors = []
        self._seniors = []

    def add_junior(self, *args):
        self._juniors.extend(args)

    def add_senior(self, *args):
        self._seniors.extend(args)

    def __iter__(self):
        for dev in self._juniors:
            yield dev, "junior"
        for dev in self._seniors:
            yield dev, "senior"


class AttrsIterator:
    def __init__(self, obj):
        self.obj = obj
        self._attrs_iterator = iter(self.obj.__dict__.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._attrs_iterator)


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class SkipIterator:
    def __init__(self, iterable, n: int):
        self._iter = (
            x for i, x in enumerate(iter(iterable)) if not n or i % (n + 1) == 0
        )

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._iter)


skipiterator = SkipIterator(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1
)  # пропускаем по одному элементу

print(*skipiterator)
skipiterator = SkipIterator(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2
)  # пропускаем по два элемента

print(*skipiterator)
skipiterator = SkipIterator(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0
)  # не пропускаем элементы

print(*skipiterator)
