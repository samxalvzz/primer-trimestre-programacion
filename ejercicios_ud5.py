"""
Ejercicio 1.

Los médicos forenses utilizan la longitud de los huesos para determinar la altura de una
persona, cuando la persona estaba viva.

Por ejemplo, para los varones:
altura (en cm) = 69.089 + 2.232 × longitud de la tibia

Para las mujeres, el valor es el siguiente:
altura (en cm) = 61.412 + 2.317 × longitud de la tibia

A partir de los 30 años (inclusive), la altura de una persona decrece a una tasa de 0.06
cm por año.

Escribir un programa que, dados los valores de la longitud de la tibia, el sexo y la edad
del paciente, nos calcule la altura aproximada.
"""

# Primero, vamos a poner todos los datos:
longitud_tibia: float = 3.0
sexo: str = 'M'         # 'V' = Varón, 'M' = Mujer
edad: int = 30

# Ahora vamos a poner los datos intermedios
altura_varon: float = 69.089 + 2.232 * longitud_tibia
altura_mujer: float = 61.412 + 2.317 * longitud_tibia

# Calculamos la altura previa al decrecimiento por año:
altura_base: float = altura_varon if sexo == 'V' else altura_mujer

# Calculamos la altura final:
altura: float = altura_base if edad < 30 else altura_base - 0.06 * (edad - 29)

"""
Ejercicio 2.
Escribir un programa que calcule el volumen de una esfera a partir de su radio, usando la siguiente formula: 𝑉 = 4/3 𝜋𝑟³

"""

from math import math 

radio: float = 5.0                                  # El radio de la esfera
volumen: float = (4 / 3) * math.pi * (radio ** 3)   # El volumen de la esfera 

"""
Ejercicio 3.
Escribir un programa que compruebe si tres datos de entrada tienen el mismo valor.

"""

a = input("Introduzca el siguiente número: ")
b = input("Introduzca el siguiente número: ")
c = input("Introduzca el siguiente número: ")

if a == b == c:
    print("Los tres valores son iguales.")
else:
    print("Los tres valores NO son iguales.")

"""
Ejercicio 4.
Escribir un programa que compruebe si cuatro datos de entrada tienen el mismo valor

"""
a = input("Introduzca el siguiente número: ")
b = input("Introduzca el siguiente número: ")
c = input("Introduzca el siguiente número: ")
d = input("Introduzca el siguiente número: ")

if a == b == c:
    print("Los tres valores son iguales.")
else:
    print("Los tres valores NO son iguales.")

"""
Ejercicio 5.
Escribir un programa que reciba dos datos de entrada y que los ordene de menor a
mayor, indicando cuál es el primero y cuál el segundo.

"""

a = float(input("Ingrese por favor el primer número: "))
b = float(input("Ingrese por favor el segundo número: "))

# Ahora vamos a ordenar y mostrar los datos:
if a < b:
    print(f"El primer número es: {a}")
    print(f"El segundo número es: {b}")
elif b < a:
    print(f"El primer número es: {b}")
    print(f"El segundo número es: {a}")
else: 
    print("Ambos números son iguales", a)

"""
Ejercico 6.
Escribir un programa que reciba tres datos de entrada y que los ordene de menor a
mayor, indicando cuál es el primero, cuál el segundo y cuál el tercero.

"""

a = float(input("Ingrese por favor el primer número: "))
b = float(input("Ingrese por favor el segundo número: "))
c = float(input("Ingrese por favor el tercer número: "))

# Ahora vamos a ordenar y mostrar los datos:
if a < b:
    print(f"El primer número es: {a}")
    print(f"El segundo número es: {b}")
elif b < a:
    print(f"El primer número es: {b}")
    print(f"El segundo número es: {a}")
else: 
    print("Ambos números son iguales", a)