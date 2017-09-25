x_max = 4
y_max = 3
goal = 2


class demo:
    x = 0
    y = 0

    def __init__(self, x, y):
        demo.x = x
        demo.y = y
        print(demo.x, demo.y)

    def fill(self):
        demo.x = x_max
        print(demo.x, demo.y)

    def por(self):
        while demo.x > 0 and demo.y < y_max:
            demo.x -= 1
            demo.y += 1
        print(demo.x, demo.y)

    def drop(self):
        demo.y = 0
        print(demo.x, demo.y)


a = demo(4, 3)

while True:
    if demo.x == goal or demo.y == goal:
        break
    a.por()

    if demo.x == goal or demo.y == goal:
        break
    if demo.x == 0:
        a.fill()

    if demo.y == y_max:
        if demo.x == goal or demo.y == goal:
            break
        a.drop()

    if demo.x != x_max:
        if demo.x == goal or demo.y == goal:
            break
        a.por()
