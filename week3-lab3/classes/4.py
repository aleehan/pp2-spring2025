class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        return (self.x, self.y)
    
    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def dist(self, b):
        return ((b.x - self.x)**2+(b.y - self.y)**2)**0.5


a = Point(1, 5)
print(a.show())

b = Point(10, 50)
print(b.show())

print(a.dist(b))