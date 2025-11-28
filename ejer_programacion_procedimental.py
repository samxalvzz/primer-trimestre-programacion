def cuadrado(n: int) -> None:
    """
    Imprime un cuadrado usando asteriscos con el numero de lineas y columnas indicado.
    
    Args:
        n (int): El numero de lineas (y columnas) deseado.
    
    Returns:
        None
        
    >>> cuadrado(1)
    *
    >>> cuadrado(2)
    **
    **
    >>> cuadrado(3)
    ***
    ***
    ***
    >>> cuadrado(5)
    *****
    *****
    *****
    *****
    *****
    """
    i = 0
    while i < n:
        print('*' * n)
        i += 1