def unicos(lista):
    """
    Hacer una función recursiva que reciba una funcion llamada(secuencia)
    que reciba una secuencia de numeros enteros en la que todos
    aparecen dos o mas veces, excepto dos de ellos que solo aparecen una vez.
    La funcion debera devolver una lista que contenga solo esos dos elementos unicos.
    >>> unicos([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])
    [1, 2]
    >>> unicos([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])
    [5, 6]
    >>> unicos([4, 3, 9, 9, 1, 1, 6, 1, 6, 2, 4])
    [2, 3]
    """
    res: list[int] = []
    i = 0
    while i < len(lista):
        if lista.count(lista[i]) == 1:
            res.append(lista[i])
        i += 1
    return res

# Esto es recursiva

def unicos(lista: list[int]) -> list[int]:
    def aux(l, res, vistos):
        if len(l) == 0:
            return res
        if l[0] in visto:
            return aux(l[1:], res, vistos)
        elif l[0] not in res and l[0] not in l[1:]:
            return aux(l[1:], res + [l[0]], vistos + [l[0]])
        else:
            return aux(lista, [1:], res, visto + [l[0]])
    return aux(lista, [], [])
    
