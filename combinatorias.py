def comb(n: int, k: int) -> int:
    if k == 0 or n == k:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)

def triangulo(num_lineas: int) -> None:
    """Imprime el triangulo de Tartaglia con el numero de lineas indicado"""
    n = 0
    while n < num_lineas:
        k = 0
        while k <= num_lineas:
            print(comb_iter(n, k), end =" ")
            k += 1
        print()
        n += 1

def matriz_identidad(n: int) -> list[list[int]]:
    """Devuelve la matriz identidad de tamaño n x n."""
    res: list[list[int]] = []
    i = 0
    while i < n:
        fila: list[int] = []
        j = 0
        while j < n:
            fila.append(1 if i == j else 0)
            j +=1
        res.append(fila)
        i += 1
    return res

def imprimir_matriz(m: list[list]) -> None:
    """Imprime una matriz."""
    fila = 0
    while fila < len(m):
        col = 0
        while col < len(m[fila]):
            print(m[fila][col], end=' ')
            col += 1
        fila += 1
        print()
        
def escalar(k: int, m: list[list[int]]) -> list[list[int]]:
    """
    Devuelve una nueva matriz multiplicando todos los elementos
    de la matriz original por el valor k.
    >>> escalar(3, [[1, 2], [4, 5]])
    [[3, 6], [12, 15]]
    """
    res: list[list[int]] = []
    i = 0
    while i < len(m):
        fila_nueva: list[int] = [] 
        j = 0
        while j < len(m[i]):
            fila_nueva.append(k * m[i][j])
            j += 1
        res.append(fila_nueva)
        i += 1
    return res    
    

def traspuesta(m: list[list[int]]) -> list[list[int]]:
    """
    Devuelve la traspuesta de una matriz.
    >>> traspuesta([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    j = 0
    res: list[list[int]] = []
    while j < len(m[0]):
        i = 0
        fila: list[int] = []
        while i < len(m):
            fila.append(m[i][j])
            i += 1
        res.append(fila)
        j += 1
    return res


def magico(n: int) -> list[list[int]]:
    """
    Devuelve el cuadrado mágico n x n.
    """
    res: list[list[int]] = []
    while len(res) < n:
        res.append([0] * n)
    i = 0
    j = n // 2
    k = 1
    while k <= n * n:
        res[i][j] = k
        nuevo_i, nuevo_j = (i - 1) % n, (j + 1) % n
        if res[nuevo_i][nuevo_j] != 0:
            nuevo_i, nuevo_j = (i + 1) % n, j
        i, j = nuevo_i, nuevo_j
        k += 1
    return res
    