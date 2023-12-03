def add(*args) -> any:
    try:
        return sum(args)
    except TypeError:
        return "The value should contain only type='int' with base 10"


def subt(first: int, second: int, reverse: bool = False, _abs: bool = False) -> any:
    try:
        if not reverse:
            return abs(first - second) if _abs else first - second
        return abs(second - first) if _abs else second - first
    except TypeError:
        return "The value should contain only type='int' with base 10"


def mult(*args, _abs: bool = False) -> any:
    try:
        ans = 1
        _list = list(args)
        for i in _list:
            if type(i) is int:
                ans *= i
            else:
                return "The value should contain only type='int' with base 10"
        return abs(ans) if _abs else ans
    except TypeError:
        return "The value should contain only type='int' with base 10"


def div(first: float, second: float, _isint: bool = False, _abs: bool = False) -> any:
    try:
        ans = first / second
        return (
            abs(int(ans) if _isint else ans) if _abs else (int(ans) if _isint else ans)
        )
    except ZeroDivisionError:
        return "Value cannot be divided by 0"
