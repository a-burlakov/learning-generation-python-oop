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
