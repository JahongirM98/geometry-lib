import math
import pytest
from geometry.shapes.triangle import Triangle

def test_triangle_area_and_right():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0, rel_tol=1e-12)
    assert t.is_right() is True

@pytest.mark.parametrize("sides", [(2, 2, 3), (5.5, 6.1, 7.2)])
def test_triangle_valid_non_right(sides):
    t = Triangle(*sides)
    assert t.area() > 0
    assert t.is_right() is False

@pytest.mark.parametrize("sides", [(0, 1, 1), (-1, 2, 2), (1, 2, 3), (1, 10, 12)])
def test_triangle_invalid_sides(sides):
    with pytest.raises(ValueError):
        Triangle(*sides)
