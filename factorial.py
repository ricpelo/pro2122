"""
Módulo del factorial.
"""

def fact(n):
    """
    Calcula el factorial de un número.

    Args:
        n (int): El número sobre el que se calcula el factorial.

    Returns:
        int: El factorial de n.

    >>> fact(5)
    120
    >>> fact(4)
    24
    >>> fact(0)
    1
    """
    def fact_iter(acc):
        nonlocal n
        if n == 0:
            return acc

        acc *= n
        n -= 1
        return fact_iter(acc)
    return fact_iter(1)
