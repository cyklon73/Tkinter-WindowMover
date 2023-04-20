class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x:{self.x},y:{self.y}"

    def num(self) -> (float, float):
        return self.x, self.y

    def add(self, x=0, y=0):
        self.x += x
        self.y += y
        return self

    def subtract(self, x=0, y=0):
        self.x -= x
        self.y -= y
        return self

    def multiply(self, x=1, y=1):
        self.x *= x
        self.y *= y
        return self

    def divide(self, x=1, y=1):
        self.x /= x
        self.y /= y
        return self
