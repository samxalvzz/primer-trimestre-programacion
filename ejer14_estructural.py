"""
14. Convertir una cantidad de tiempo (en segundos, Z) en la correspondiente en horas,
minutos y segundos, con arreglo al siguiente formato:
3817 segundos = 1 horas, 3 minutos y 37 segundos
"""

Z = int(input("Introduce la cantidad de segundos: "))

horas = Z // 3600
resto = Z % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{Z} segundos = {horas} horas, {minutos} minutos y {segundos} segundos")
