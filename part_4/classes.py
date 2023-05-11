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
