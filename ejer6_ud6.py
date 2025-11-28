"""
Ejercicio 6.
Escribir una función que reciba una cantidad de días, minutos y segundos, y que calcule
y devuelva el número de segundos en los datos de entrada indicados. Dar un ejemplo
de uso.

"""

def cuenta_segundos(dias, minutos, segundos):
    total_segundos = dias * 24 * 60 * 60 + minutos * 60 + segundos
    return total_segundos

# Un ejemplo:
dias = 3
minutos = 30
segundos = 50

resultado = cuenta_segundos(dias, minutos, segundos)
print(f"En {dias}, {minutos}, y {segundos} hay {resultado} segundos.")

# Otra manera más corta de hacerla es la siguiente:
segundos = lambda dias, minutos, segundos: 86400 * dias + 60 * minutos + segundos
ejemplo = segundos(5, 27, 6)


