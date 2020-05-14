class Snail:
    def __init__(self, color, size, speed):
        self.color, self.size, self.speed = color, size, speed

    def __str__(self):
        return 'Snail {} - {}'.format(self.color, self.size)

    def crawl(self, time):
        way = time * self.speed
        self.speed -= (way // 10)
        return way

    def get_through(self, dimensions):
        return dimensions >= self.size

    def leave_trace(self):
        return '*' * (self.speed * self.size // 2)

    def __gt__(self, other):  # >
        if self.size > other.size:
            return True
        else:
            return False

    def __ge__(self, other):  # >=
        if self.size > other.size:
            return True
        else:
            return False

    def __lt__(self, other):  # <
        if self.size < other.size:
            return True
        else:
            return False

    def __le__(self, other):  # <=
        if self.size < other.size:
            return True
        else:
            return False

    def __eq__(self, other):  # ==
        if (self.size == other.size) and (self.speed == other.speed) and (self.color == other.color):
            return True
        else:
            return False

    def __ne__(self, other):  # !=
        if self.size != other.size:
            return True
        else:
            return False
