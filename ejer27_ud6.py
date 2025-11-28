"""
Ejercicio 27.
27. La función mayor tiene la siguiente especificación:
Pre : 𝑡 ≠ ()
mayor(𝑡: tuple[𝛼]) -> 𝛼
Post : mayor(𝑡) = el mayor elemento de 𝑡
Por ejemplo: mayor((3, 2, 5, 7)) == 7.
Escribir una función recursiva que satisfaga dicha especificación.
"""

# max2(a, b) =
#   a if  a>= b else b

# caso base: mayor(t) = t[0], si len(t)== 1
# reducción: t[1:], si len(t) > 1
# pensamiento optimista: mayor(t) = max2(t[0]mayor(t[1:]))

max2 = lambda a, b: a if a >= b else b
mayor = lambda t: t[0] if len(t) == 1 else max2(t[0], mayor(t[1:]))

