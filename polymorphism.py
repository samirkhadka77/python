class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = circle(21)

print("area of circle is ", c1.area())

print("perimeter of circle is ", c1.perimeter())