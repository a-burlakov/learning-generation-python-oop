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


def non_closed_files(files):
    return [file for file in files if not file.closed]


def log_for(logfile, date_str):
    with (
        open(logfile, "r", encoding="utf-8") as file,
        open(f"log_for_{date_str}.txt", "w", encoding="utf-8") as file_result,
    ):
        for line in file.readlines():
            if line.startswith(date_str):
                new_line_in_result = line.replace(date_str, "").lstrip()
                file_result.write(new_line_in_result)


def is_context_manager(obj):
    return all(x in dir(obj) for x in ["__enter__", "__exit__"])


class SuppressAll:
    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_value, trace):
        return True


class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"До встречи, {self.name}!")


class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
        except AttributeError:
            print("Незакрываемый объект")


class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "r", encoding="utf-8")
        return self.file.read().split("\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self.file.readlines()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class Suppress:
    def __init__(self, *exceptions):
        self.suppressed_exceptions = exceptions
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.exception = exc_val
        return exc_type in self.suppressed_exceptions


with Suppress(TypeError, ValueError) as context:
    number = int("я число")


from time import perf_counter


class AdvancedTimer:
    def __init__(self):
        self.runs = []
        self.last_run = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.last_run = perf_counter() - self.start
        self.runs.append(self.last_run)

    @property
    def min(self):
        if not self.runs:
            return None
        return min(self.runs)

    @property
    def max(self):
        if not self.runs:
            return None
        return max(self.runs)


class UpperPrint:
    def __enter__(self):
        import sys

        self.original_write = sys.stdout.write
        sys.stdout.write = self.upper_write

    def upper_write(self, text):
        self.original_write(text.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys

        sys.stdout.write = self.original_write


from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    def upper_write(text):
        original_write(text[::-1])

    original_write = sys.stdout.write
    sys.stdout.write = upper_write
    yield
    sys.stdout.write = original_write


from keyword import kwlist


class NonNegativeInteger:
    def __init__(self, attr, default=None):
        self._attr = attr
        self.default = default

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        elif obj.default is not None:
            return self.default
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError("Некорректное значение")


class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, times):
        self.max_times = times
        self.count_times = 0

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value

    def __get__(self, obj, cls):

        if self.count_times >= self.max_times:
            raise MaxCallsException("Превышено количество доступных обращений")

        self.count_times += 1

        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")


class TypeChecked:
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __init__(self, *types):
        self.types = types

    def __set__(self, obj, value):
        if any(isinstance(value, t) for t in self.types):
            obj.__dict__[self._attr] = value
        else:
            raise TypeError("Некорректное значение")

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError("Атрибут не найден")


class Student:
    name = TypeChecked(str)


student = Student()
student.name = "Mary"

try:
    student.name = 99
except TypeError as e:
    print(e)

print(student.name)
