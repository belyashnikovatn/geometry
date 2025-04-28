# Geometry Library
Geometry — это лёгкая и расширяемая Python-библиотека для вычисления площадей геометрических фигур.
Поддерживает окружности, треугольники (с возможностью проверки на прямоугольность) и легко расширяется под новые фигуры.

# Установка
```bash
pip install .
```

# Основные возможности
- Вычисление площади круга по радиусу.
- Вычисление площади треугольника по трём сторонам (формула Герона).
- Проверка, является ли треугольник прямоугольным.
- Работа через общий интерфейс для всех фигур.
- Расширение под новые фигуры.

# Запуск тестов
```bash
python -m unittest discover -s tests
```

# Как добавить новую фигуру
1. Создать новый класс, унаследованный от Figure.
2. Реализовать метод area().
3. (Опционально) Добавить специфические методы.

```python
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError('Side must be positive.')
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
```

# Лицензия
MIT License.

# Авторство
[Беляшникова Таня](https://github.com/belyashnikovatn)