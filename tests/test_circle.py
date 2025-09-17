import math
import pytest
from geometry.shapes.circle import Circle

def test_circle_area_pi():
    c = Circle(1)
    assert math.isclose(c.area(), math.pi, rel_tol=1e-12)

@pytest.mark.parametrize("r", [0, -1, -5.5])
def test_circle_invalid_radius(r):
    with pytest.raises(ValueError):
        Circle(r)
