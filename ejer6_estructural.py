"""
6. Escribir un programa que muestre por pantalla la tabla de multiplicar de un número
comprendido entre 0 y 10, introducido por teclado.
"""
numero = int(input("Introduce un numero entre 0 y 10: "))

if 0 <= numero <= 10:
    i = 0
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
else:
    print("Numero fuera del rango permitido")
    