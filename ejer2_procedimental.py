"""
Escribir tres funciones que impriman las siguientes salidas en función de la cantidad de
líneas que se desean ( es un espacio en blanco):
***** * *
***** * ***
***** * *****
***** * *******
***** * *
"""
# ARBOLES

def arbol1(n: int) -> None:
    def ancho(num: int) -> int:
        return 2 * num - 1
    if n == 0:
        pass
    elif n == 1:
        print("*")
    else:
        i = 1
        while i < n:
            print(("*" * ancho(i)).center(ancho(n), "¬"))
            i += 1
        print("*".center(ancho(n), "¬"))
        
        
def arbol2(n: int) -> None:
    def ancho(num: int) -> int:
        return 2 * num - 1
    if n == 0:
        pass
    else:
        i = 1
        while i < n:
            print(("*" * ancho(i)).center(ancho(n), "¬"))
            i += 1
        print("*".center(ancho(n), "¬"))
        

def arbol3(n: int) -> None:
    def ancho(num: int) -> int:
        return 2 * num - 1
    if n > 0:
        i = 1
        while i < n:
            print(("*" * ancho(i)).center(ancho(n), "¬"))
            i += 1
        print("*".center(ancho(n), "¬"))
        
        
        
def arbol4(n: int) -> None:
    def ancho(num: int) -> int:
        return 2 * num - 1
    if n > 0:
        an = ancho(n)
        i = 1
        while i < n:
            print(("*" * ancho(i)).center(an, "¬"))
            i += 1
        print("*".center(an, "¬"))
        

def arbol5(n: int) -> None:
    def ancho(num_lineas: int) -> int:
        return 2 * num_lineas - 1
    def imprime_linea(num_linea: int, anch: int) -> None:
        print(("*" * ancho(num_linea)).center(anch, "¬"))
        
    if n > 0:
        an = ancho(n)
        i = 1
        while i < n:
            imprime_linea(i, an)
            i += 1
        imprime_linea(1, an)