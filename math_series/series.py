"""
The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two.
"""


def fibonacci(n):
    # return nth value (0)
    if type(n) != int:
        return 'Invalid Input'

    if n == 0:
        return 0

    if n == 1:
        return 1

    else:
        return n*(fibonacci(n - 1))


# -------------------------------------------
"""
start with the values 2 and 1 rather than 0 and 1
"""


def lucas(n):
    if type(n) != int:
        return 'Invalid Input'

    if n == 0:
        return 2

    if n == 1:
        return 1

    else:
        return n*(lucas(n - 1))


# --------------------------------------------
"""
  The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced
"""


def sum_series(n, op1, op2):
    op1 = 0
    op2 = 1

    if op1 == 0 and op2 == 1:
        return fibonacci(n)

    if op1 == 1 and op2 == 2:
        return lucas(n)

    else:
        if op1 > 1 and op2 > 2:
            return sum_series(n-1, op1, op2) + sum_series(n-2, op1, op2)

# --------------------------------------------
