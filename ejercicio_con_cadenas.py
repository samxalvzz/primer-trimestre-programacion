"""
Ejercicio con cadenas.

pre: true
Longitud(s:str) --> int
post: longitud(s) = len(s)

1º caso base: longitud("") = 0
2º reduccion: s [1:]
3º pensamiento optimista: sino sé de "hola", lo reduzco con "ola"), longitud ("ola") = 3
"""

longitud = lambda s: 0 if s == "" else 1 + longitud(s[1:])