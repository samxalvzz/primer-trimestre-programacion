"""
15. Escribir un programa que, en primer lugar, lea los coeficientes 𝑎2 , 𝑎1 y 𝑎0 de un polinomio
de segundo grado
𝑎2𝑥
2 + 𝑎1𝑥 + 𝑎0
y escriba ese polinomio. Y, en segundo, lea el valor de 𝑥 y escriba qué valor toma el
polinomio para esa 𝑥.
Para facilitar la salida, se supondrá que los coeficientes y 𝑥 son enteros. Por ejemplo, si
los coeficientes y 𝑥 son 1, 2, 3 y 2, respectivamente, la salida puede ser:
1x^2 + 2x + 3
p(2) = 9
"""

a2 = int(input("Introduce el coeficiente a2: "))
a1 = int(input("Introduce el coeficiente a1: "))
a0 = int(input("Introduce el coeficiente a0: "))

print(f"{a2}x^2 + {a1}x + {a0}")

x = int(input("Introduce el valor de x: "))

p_x = a2 * x**2 + a1 * x + a0

print(f"p({x}) = {p_x}")