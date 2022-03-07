class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)

    def get_distance_between(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** (1/2)


first_point = Point(2, 1)
second_point = Point(1, 4)
print(f"Длина первого вектора: {first_point.get_distance()}")
print(f"Длина второго вектора: {second_point.get_distance()}")
print(f"Расстояние между точками: {first_point.get_distance_between(second_point)}")
