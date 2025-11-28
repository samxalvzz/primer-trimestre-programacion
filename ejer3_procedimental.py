"""
3. Escribir una función para hallar
𝑛
𝑘

, donde 𝑛 y 𝑘 son datos enteros positivos,
a. mediante la fórmula 𝑛!
(𝑛−𝑘)!𝑘!
b. mediante la fórmula 𝑛(𝑛−1)···(𝑘+1)
(𝑛−𝑘)!
¿Qué ventajas presenta la segunda con respecto a la primera?
"""

def comb1(n, k):
    def fact(x):
        fact = 1
        i = 1
        while i <= x:
            fact *= i
            i += 1
        return fact
    
    return fact(n) // (fact(k) * fact(n - k))

def comb2(n, k):
    n = 1
    i = 0
    while i < k:
        n *= (n - i)
        i += 1
    
    d = 1
    j = 1
    while j <= k:
        d *= j
        j += 1
    
    return n // d

# Otra version

def fact(n: int) -> int:
    """Devulve el factorial de n."""
    """i = 1
    prod = 1
    while i <= n:
        prod *= i
        i += 1
    return prod"""

    return medio_fact(n, 0)
""">>> fact(5)
120"""

def medio_fact(n: int, k: int) -> int:
    i = k + 1
    prod = 1
    while i <= n:
        prod *= i
        i += 1
    return prod
""">>> medio_fact(8, 3)
6720"""

#def comb(n: int, k :int) -> int:
    #return fact(n) // (fact(k) * fact(n - k))
    #return medio_fact(n, k) // fact(n - k)
""">>> comb(8, 3)
56"""

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
        
            


    