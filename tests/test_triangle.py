from geometry.shapes.triangle import Triangle

def test_triangle_smoke():
    t = Triangle(3,4,5)
    assert hasattr(t, "area")
    assert hasattr(t, "is_right")
