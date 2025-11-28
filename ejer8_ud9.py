"""
8. Escribe un programa que solicite al usuario su edad y le indique si es mayor de edad
(mediante un mensaje Sí o No).
"""

edad: int = int(input('Introduzca su edad: '))
print('Sí' if edad >= 18 else 'No')