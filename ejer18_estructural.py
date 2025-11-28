"""
18. Para hallar en qué fecha cae el Domingo de Pascua de un anyo cualquiera, basta con
hallar las cantidades a y b siguientes:
a = (19 * (anyo % 19) + 24) % 30
b = (2 * (anyo % 4) + 4 * (anyo % 7) + 6 * a + 5) % 7
y entonces, ese Domingo es el 22 de marzo + a + b días, que podría caer en abril. Escriba
un programa que realice estos cálculos, produciendo una entrada y salida claras.
"""

anyo = int(input("Introduce el año: "))

a = (19 * (anyo % 19) + 24) % 30
b = (2 * (anyo % 4) + 4 * (anyo % 7) + 6 * a + 5) % 7

dia = 22 + a + b

if dia > 31:
    mes = "abril"
    dia -= 31
else:
    mes = "marzo"

print(f"El Domingo de Pascua en {anyo} cae el {dia} de {mes}.")
