import math

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

x, y, z = input("Введите длины сторон треугольника через пробел: ").strip().split()
x, y, z = map(float, (x, y, z))
while x + y <= z or x + z <= y or y + z <= x:
    print("Треугольник с такими длинами сторон не существует!")
    x, y, z = input("Введите длины сторон треугольника через пробел: ").strip().split()
    x, y, z = map(float, (x, y, z))
    
print(f"Площадь треугольника равна: {triangle_area(x, y, z)}")

