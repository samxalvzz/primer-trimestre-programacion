"""
8. Escribir un programa que calcule la media de cinco valores numéricos reales (tipo float)
introducidos por teclado.
"""
print("Introduce unos cincos valores numéricos reales: ")

v1 = float(input("Introduce el primer valor numérico: "))
v2 = float(input("Introduce el segundo valor numérico: "))
v3 = float(input("Introduce el tercer valor numérico: "))
v4 = float(input("Introduce el cuarto valor numérico: "))
v5 = float(input("Introduce el quinto valor numérico: "))

media = (v1 + v2 + v3 + v4 + v5) / 5

print("La media es:", media)