from Mathcom import subt, add, div, mult


def test_basics():
    assert add(1, 2, 3) == 6
    assert subt(5, 3, True, True) == 2
    assert mult(2, -3, 5) == -30
    assert mult("a", 2, 3) == "The value should contain only type='int' with base 10"
    assert div(10, -2) == -5
