"""
11. Escribir un programa que determine si un número entero introducido por teclado es
primo o compuesto.
Indicación: Un número primo es aquel que sólo puede dividirse exactamente por sí
mismo y por 1.
"""

n = int(input("Introduce un numero entero: "))

if n < 2:
    print ("El numero no es ni primo ni compuesto.")
else:
    es_primo = True
    
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print("El numero es primo")
    else:
        print("El numero es compuesto")