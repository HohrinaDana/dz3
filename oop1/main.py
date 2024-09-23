import math

class Rectangle:
    def __init__(self, a, b, x, y):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.a) + 'x' + str(self.b) + ' координаты левого нижнего угла: ' + str(self.x) + ',' + str(self.y)

    def square(self):
        return self.a * self.b

    def intersection(self, rect2):
        rect3_a = min(self.x + self.a, rect2.x + rect2.a) - max(self.x, rect2.x)
        rect3_b = min(self.y + self.b, rect2.y + rect2.b) - max(self.y, rect2.y)

        if rect3_a > 0 and rect3_b > 0:
            return rect3_a * rect3_b
        return 0 #Если не пересекаются

class Circle:
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.r) + ' координаты центра: ' + str(self.x) + ',' + str(self.y)

    def square(self):
        return math.pi * self.r ** 2

    def intersection(self, circ2):
        r1, r2 = self.r, circ2.r
        dist = math.sqrt((self.x - circ2.x) ** 2 + (self.y - circ2.y) ** 2) #Расстояние между центрами

        if dist >= r1 + r2:  #Если не пересекаются
            return 0
        elif dist <= abs(r1 - r2):  #Если круг внутри другого
            return math.pi * min(r1, r2) ** 2
        else:
            f1 = 2 * math.acos(((r1 * r1) - (r2 * r2) + (dist * dist)) / (2 * r1 * dist))
            f2 = 2 * math.acos(((r2 * r2) - (r1 * r1) + (dist * dist)) / (2 * r2 * dist))
            s1 = ((r1 * r1) * (f1 - math.sin(f1))) / 2
            s2 = ((r2 * r2) * (f2 - math.sin(f2))) / 2

            return s1 + s2

rectangle1 = Rectangle(4, 3, 0, 0)
rectangle2 = Rectangle(3, 3, 3, 1)

circle1 = Circle(7, 0, 0)
circle2 = Circle(4, 3, 0)

print(rectangle1.intersection(rectangle2)) #Площадь пересечения прямоугольников
print(circle1.intersection(circle2)) #Площадь пересечения кругов
