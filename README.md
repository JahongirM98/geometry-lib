# geometry-lib

Мини-библиотека на Python для вычисления площадей фигур и проверки треугольника на прямоугольность.  
Сделана для тестового задания Mindbox.

## Возможности
- Вычисление площади круга по радиусу
- Вычисление площади треугольника по трём сторонам (формула Герона)
- Проверка, является ли треугольник прямоугольным
- Архитектура с абстрактным базовым классом `Shape`, легко расширяемая новыми фигурами

## Установка и запуск
```bash
# 1. Клонируем проект
git clone git@github.com:<username>/geometry-lib.git
cd geometry-lib

# 2. Создаём виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Запускаем тесты
pytest -q
```

## Пример использования
```python
from geometry.shapes.circle import Circle
from geometry.shapes.triangle import Triangle

circle = Circle(5)
print(circle.area())  # 78.54...

triangle = Triangle(3, 4, 5)
print(triangle.area())     # 6.0
print(triangle.is_right()) # True
```

## Тестирование
```bash
pytest
```

## Дополнительно
- Код покрыт юнит-тестами (`pytest`)
- Проект оформлен в виде библиотеки (src-layout)
- Легко добавить новые фигуры без изменения существующих
