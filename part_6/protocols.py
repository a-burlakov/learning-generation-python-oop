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

    def __iter__(self):
        return iter(self.obj.__dict__.items())

    def __next__(self):
        for k, v in iter(self):
            yield k, v
        raise StopIteration


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User("Debbie", "Harry", 77)
attrsiterator = AttrsIterator(user)

for what in attrsiterator:
    print(what)
