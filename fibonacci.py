def fib_hasta(n: int) -> list[int]:
    """
    Escribir en Python una funcion pura llamada fibonacci_hasta(n) que reciba
    un número entero positivo n y devuelva una lista con todos los numeros
    de la sucesion de Fibonacci menores o iguales a n:
    >>> fibonacci_hasta(10)
    [0, 1, 1, 2, 3, 5, 8]
    >>> fibonacci_hasta(30)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    >>> fibonacci_hasta(0)
    [0]
    """
    res: list[int] = []
    act, sig = 0, 1
    while act <= n:
        res.append(act)
        act, sig = sig, act + sig
    return res
        
        