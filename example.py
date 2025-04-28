from geometry import Circle, Triangle, calculate_area

# Круг
circle = Circle(radius=5)
print(f'Площадь круга: {calculate_area(circle)}')

# Треугольник
triangle = Triangle(3, 4, 5)
print(f'Площадь треугольника: {calculate_area(triangle)}')

# Проверка прямоугольности треугольника
if triangle.is_right():
    print('Треугольник прямоугольный!')
else:
    print('Треугольник не прямоугольный.')
