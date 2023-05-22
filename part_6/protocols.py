import random


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


class RandomLooper:
    def __init__(self, *iterables):
        full_list = []
        for iterable in iterables:
            full_list.extend(list(iterable))

        random.shuffle(full_list)
        self._iter = iter(full_list)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._iter)


class Peekable:
    def __init__(self, iterable):
        self._iter = iter(iterable)
        self._iter_to_peek = iter(iterable)
        try:
            self._peek_value = next(self._iter_to_peek)
        except StopIteration:
            self._peek_value = None

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._peek_value = next(self._iter_to_peek)
        except StopIteration:
            self._peek_value = None
        return next(self._iter)

    def peek(self, default=Ellipsis):
        if self._peek_value:
            return self._peek_value
        elif default != Ellipsis:
            return default
        else:
            raise StopIteration


class SparseArray:
    def __init__(self, default):
        self.default = default
        self.array = []

    def __getitem__(self, key):
        if len(self.array) < key + 1:
            return self.default

        return self.array[key]

    def __setitem__(self, key, value):
        if len(self.array) < key + 1:
            self.array += [self.default] * (key + 1 - len(self.array))

        self.array[key] = value


class CyclicList:
    def __init__(self, iterable):
        self.cyclic_list = list(iterable)

    def __getitem__(self, item: int):
        return self.cyclic_list[item % len(self.cyclic_list)]

    def __len__(self):
        return len(self.cyclic_list)

    # def __iter__(self):
    #     while True:
    #         yield from self.cyclic_list

    def append(self, value):
        self.cyclic_list.append(value)

    def pop(self, index=Ellipsis):
        if index == Ellipsis:
            return self.cyclic_list.pop()
        else:
            return self.cyclic_list.pop(index % len(self.cyclic_list))


def print_file_content(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("Файл не найден")
