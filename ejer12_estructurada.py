"""
12. Escribir un programa que gestione datos almacenados en una lista, de forma que muestre
un menú con las siguientes opciones:
1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.
El programa deberá pedir la información necesaria para cada opción elegida por el
usuario.
"""

OPCIONES ="""1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.
"""

def imprimir_menu(opciones: str) -> None:
    """
    Muestra un menú de opciones.
    
    Args:
        opciones (str): Las opciones del menú (una cadena multilinea una opción
                        por línea).
                        
    Returns:
        None
    """
    print(opciones)


def pedir_entero(mensaje: str) -> int:
    """
    Pide un número entero al usuario y lo devuelve.
    
    Args:
        mensaje (str): El mensaje que se muestra al usuario.
        
    Returns:
        El entero introducido por el usuario.
    """
    while True:
        try:
            opc: int = int(input(mensaje))
            return opc
        except ValueError:
            print('El valor introducido no es correcto.')



def pedir_opcion() -> int:
    """
    Pide una opción del menú al usuario y la devuelve.
    
    Returns:
        El entero que representa la opción elegida
    """
    return pedir_entero('Introduzca una opción: ')


def anadir(lst: list[str]) -> None:
    """
    Añade un alemento a la lista.
    
    El elemento a añadr se pide al usuario.
    
    Args:
        lst (list[str]): La lista en la que se va añadir el elemento.
    
    Returns:
        None
    """
    valor = input('Introduzca un valor: ')
    lst.append(valor)


def pedir_posicion(lst: list) -> int:
    """
    Pide al usuario un ìndice vàlido de la lista de entrada y lo devuelve.
    
    El índice devuelto debe cumplir que: 0 <= índice < len(lst)
    
    Args:
        lst (list[str]): La lista de la que se va a extraer la posición.
        
    Returns:
        El entero que representa el índice introducido por el usuario.
    """
    while True:
        i = pedir_entero('Introduzca la posición a cambiar (contando desde 0): ')
        if i >= 0 and i < len(lst):
            return i
        print('La posición debe ser valida')

    
def cambiar(lst: list[str]) -> None:
    """
    Cambia un elemento de la lista a un valor nuevo.
    
    Tanto la posición del elemento a cambiar como el nuevo valor seŕan
    introducidos por el usuario.
    
    Si está vacía, lo advierte al usuario.
    
    Args:
        lst (list)[str]): La lista en la que se va a cambiar un elemento.
        
    Returns:
        None
    """
    if es_vacia(lst):
        return
    i = pedir_posicion(lst)
    nuevo = input('Introduzca el valor nuevo: ')
    lst[i] = nuevo


def mostrar(lst: list) -> None:
    """Muestra una lista por la salida."""
    print(lst)
    

def es_vacia(lst: list) -> bool:
    """
    Comprueba si una lista está vacía.
    
    Si está vacía, lo advierte al usuario.
    
    Args:
        lst (list): La lista.
        
    Returns:
        True si está vacía, y False si no lo está.
    
    >>> es_vacia([])
    No se puede cambiar una lista vacía
    True
    """
    if len(lst) == 0:
        print('No se puede cambiar una lista vacía.')
        return True
    False
    
        
def eliminar(lst: list) -> None:
    """
    Elimina un elemento de una lista.
    
    La posición del elemento a eliminar será introducida por el usuario
    
    Si está vacía, lo advierte al usuario.
    
    Args:
        lst (list): La lista en la cual se quiere eliminar un elemento.
        
    Returns:
        None
    """
    if es_vacia(lst):
        return
    i = pedir_posicion(lst)
    del lst[i]
    
    
def eliminar_todos(lst: list) -> None:
    """
    Elimina todos los elementos de una lista
    
    >>> l = [1, 2, 3]
    >>> eliminar_todos(l)
    >>> l
    []
    """
    lst.clear()


#Programa principal:


def main():
    imprimir_menu(OPCIONES)
    lista: list[str] = []
    while True: 
        opc: int = pedir_opcion()
    
        if opc == 1:
            anadir(lista)
        elif opc == 2:
            cambiar(lista)
        elif opc == 3:
            eliminar(lista)
        elif opc ==4:
            eliminar_todos(lista)
        elif opc == 5:
            mostrar(lista)
        elif opc == 0:
            break
        else:
            print('Opción incorrecta') 
        
main()