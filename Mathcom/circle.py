from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> any:
        return pi * self.radius**2

    def perimeter(self) -> any:
        return 2 * pi * self.radius

    def diameter(self) -> any:
        return 2 * self.radius


def area_of_circle(radius: float, _isint: bool = False, _abs: bool = True) -> any:
    try:
        ans = pi * radius**2
        return (
            abs(int(ans) if _isint else ans) if _abs else (int(ans) if _isint else ans)
        )
    except TypeError:
        return "The Radius should be type='int' base 10"


def perimeter_of_circle(radius: float, _isint: bool = False, _abs: bool = True) -> any:
    try:
        ans = 2 * pi * radius
        return (
            abs(int(ans) if _isint else ans) if _abs else (int(ans) if _isint else ans)
        )
    except TypeError:
        return "The Radius should be type='int' base 10"
