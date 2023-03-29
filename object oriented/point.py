class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __mul__(self, num):
        return Point(self.x * num, self.y * num)
    
    def __str__(self):
        return f'Point object: ({self.x},{self.y})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def distance(self, otherPoint):
        xComponent = (self.x - otherPoint.x) ** 2
        yComponent = (self.y - otherPoint.y) ** 2
        return (xComponent + yComponent) ** 0.5