def es_anagrama(c1: str, c2: str) -> bool:
    """
    Escribir en Python una funcion pura llamada es_anagrama(c1, c2) que determine
    si dos cadenas de texto son anagramas, ignorando mayusculas y minusculas.
    >>> es_anagrama('amor', 'Roma')
    True
    >>> es_anagrama('hola', 'adios')
    False
    """
    return sorted(c1.lower()) == sorted(c2.lower())