class Gun:
    def shoot(self):
        print("pif")


class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n


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
