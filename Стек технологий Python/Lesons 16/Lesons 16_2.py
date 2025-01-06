class Turtle(object):

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        return "Шаг не может быть меньше 1"
    
    def count_moves(self, x2, y2):
        return self.x - x2, self.y - y2

print(Turtle.count_moves)