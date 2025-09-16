from geometry.shapes.circle import Circle

def test_circle_area_smoke():
    assert round(Circle(1).area(), 5) == 3.14159
