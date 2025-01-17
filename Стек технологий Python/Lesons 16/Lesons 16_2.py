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
        cnt = 0
        while True:
            if self.s < x2 - self.x:
                if (x2 > 0) and self.x != x2:
                    if (x2 < self.x):
                        self.go_left()
                    elif (x2 > self.x):
                        self.go_right()
                    cnt += 1
            else:
                self.degrade()
                continue

            if self.s < y2 - self.y:
                self.degrade()
                if (y2 > 0) and self.y != y2:
                    if (y2 < self.y):
                        self.go_down()
                    elif (y2 > self.y):
                        self.go_up()
                    cnt += 1
            else:
                self.degrade()
                continue
            print(cnt)
                # print(self.x, x2)
                # print(self.y, y2)


            if self.x == x2 and self.y == y2:
                break
        return cnt


turtle = Turtle(0, 0, 6)

print(turtle.count_moves(9,10))

