import doctest

def add(a, b):
    """
    Returns the sum of two numbers.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    >>> add(10, 20)
    30
    """

    return a + b


if __name__ == "__main__":
    print(doctest.testmod())