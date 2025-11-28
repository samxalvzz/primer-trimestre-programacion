"""
Ejercicio 20.
La función ultimo tiene la siguiente especificación:
Pre : 𝑡 ≠ ()
ultimo(𝑡: tuple) -> Any
Post : ultimo(𝑡) = el último elemento de t
Escribir una función recursiva que satisfaga dicha especificación.
"""
# caso base: t[0], si len(t) == 1
# reducción: t[1], len(t) > 1
# pensamiento optimista: ultimo(t) = ultimo(t[1:])


ultimo = lambda t: t[0] if len(t) == 1 else ultimo(t[1:])


