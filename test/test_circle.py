from Mathcom import Circle
from Mathcom import area_of_circle, perimeter_of_circle


def test_circle():
    a = 1
    assert Circle(a).area() == 3.141592653589793
    assert Circle(a).perimeter() == 6.283185307179586
    assert area_of_circle(a, _isint=True) == 3
    assert perimeter_of_circle(a, _abs=True) == 6.283185307179586
    assert Circle(a).diameter() == 2
