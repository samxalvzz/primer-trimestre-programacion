def factorial(n: int) -> int:
    """Devuelve el factorial de un numero entero.

    >>> factorial(4)
    24
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
