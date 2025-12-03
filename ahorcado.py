def ahorcado(intento: str, solucion: str) -> None:
    """
    Escribir funcion ahorcado(intento) que juegue un turno del juego del ahorcado.
    Por ejemplo:
    >>> ahorcado('MANZANA', 'INFORMATICA')
    _N__MA__A
    >>> ahorcado('MATEMATICAS', 'INFORMATICA')
    I___MATICA
    >> ahorcado('INFORMATICA', 'INFORMATICA')
    ¡Ehnorabuena!
    """
    if intento == solucion:
        print('¡Ehnorabuena!')
        return
    i = 0
    while i < len(solucion):
        c = solucion[i]
        print(c if c in intento else '_', end='')
        i += 1
    print()

        
        
        
    
    