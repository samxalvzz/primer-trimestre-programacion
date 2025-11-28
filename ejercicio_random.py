"""
Ejercicio.

Pre >= 0 (mayor igual que 0)
digitos(n : int) -> int
post: digitos(n) = el nº de dígitos de n
"""


digitos = lambda n: 1 if n < 10 else 1 + digitos(n // 10)

