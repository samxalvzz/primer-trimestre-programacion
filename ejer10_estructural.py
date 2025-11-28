"""
10. Escribir un programa que calcule el máximo común divisor de dos números enteros
introducidos por teclado, usando:
a) La función math.gcd.
b) Bucles.
"""
# Version a)

import math

a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))

mcd = math.gcd(a, b)

print("El MCD es:", mcd)

# Version b)

a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))

while b != 0:
    a, b = b, a % b

print("El MCD es:", mcd)