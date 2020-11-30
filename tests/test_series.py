from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_five():
    actual = fibonacci(5)
    expected = 5*4*3*2*1
    assert actual == expected

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


# ----------------------------------------------

def test_fivez():
    actual = lucas(5)
    expected = 5*4*3*2*1
    assert actual == expected

def test_onez():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_zeroz():
    actual = lucas(0)
    expected = 2
    assert actual == expected


# -----------------------------------------------


def test_five1():
    actual = sum_series(5,5,5)
    expected = 5*4*3*2*1
    assert actual == expected

def test_four_all():
    actual = sum_series(4,4,4)
    expected = 4*3*2*1
    assert actual == expected

def test_one2():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_zero2():
    actual = lucas(0)
    expected = 2
    assert actual == expected