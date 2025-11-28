"""
XX. Escribe un programa que solicite al usuario 5 notas y que devuelva la media.
"""

nota1:float = float(input('Introduzca nota: '))
nota2:float = float(input('Introduzca nota: '))
nota3:float = float(input('Introduzca nota: '))
nota4:float = float(input('Introduzca nota: '))
nota5:float = float(input('Introduzca nota: '))

media: float = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print('La media es', media)