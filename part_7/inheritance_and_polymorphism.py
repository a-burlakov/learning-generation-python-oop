class Vehicle:
    ...


class LandVehicle(Vehicle):
    ...


class WaterVehicle(Vehicle):
    ...


class AirVehicle(Vehicle):
    ...


class Car(LandVehicle):
    ...


class Motocycle(LandVehicle):
    ...


class Bicycle(LandVehicle):
    ...


class Propeller(AirVehicle):
    ...


class Jet(AirVehicle):
    ...


class Shape:
    ...


class Circle(Shape):
    ...


class Polygon(Shape):
    ...


class Quadrilateral(Polygon):
    ...


class Triangle(Polygon):
    ...


class Parallelogram(Quadrilateral):
    ...


class Rectangle(Parallelogram):
    ...


class Square(Rectangle):
    ...


class IsoscelesTriangle(Triangle):
    ...


class EquilateralTriangle(Triangle):
    ...


# # # # # # # # # # # # # # # # # #


class Animal:
    def sleep(self):
        ...

    def eat(self):
        ...


class Fish(Animal):
    def swim(self):
        ...


class Bird(Animal):
    def lay_eggs(self):
        ...


class FlyingBird(Bird):
    def fly(self):
        ...


# # # # # # # # # # # # # # # #


class User:
    def __init__(self, name):
        self.name = name

    def skip_ads(self):
        return False


class PremiumUser(User):
    def skip_ads(self):
        return True


# # # # # # # # # # # # # # # #


class Validator:
    def __init__(self, obj: object):
        self.obj = obj

    def is_valid(self):
        return None


class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self.obj, (int, float))


# # # # # # # # # # # # # # # #


class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, number=1):
        self.value += number

    def dec(self, number=1):
        self.value -= number
        self.value = max(self.value, 0)


class NonDecCounter(Counter):
    def dec(self, number=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        self.value = start
        self.limit = limit

    def inc(self, number=1):
        self.value += number
        self.value = min(self.value, self.limit)


# # # # ## # # # #
