"""
16. Escribir un programa apropiado para cada una de las siguientes tareas:
a. Pedir los dos términos de una fracción y dar el valor de la división correspondiente,
a no ser que sea nulo el hipotético denominador, en cuyo caso se avisará del error.

b. Pedir los coeficientes de una ecuación de segundo grado y dar las dos soluciones
correspondientes, comprobando previamente si el discriminante es positivo o no.

c. Pedir los coeficientes de la recta 𝑎𝑥 + 𝑏𝑦 + 𝑐 = 0 y dar su pendiente y su ordenada
en el origen en caso de que existan, o el mensaje apropiado en otro caso.

d. Pedir un número natural 𝑛 y dar sus divisores.
"""
import math

while True:
    print("\nElige una opción:")
    print("1. División de fracciones")
    print("2. Ecuación de segundo grado")
    print("3. Recta ax + by + c")
    print("4. Divisores de un número natural")
    print("5. Salir")
    
    opcion = input("Introduce el número de la opción: ")

    if opcion == "1":
        numerador = float(input("Introduce el numerador: "))
        denominador = float(input("Introduce el denominador: "))
        if denominador == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            print("Resultado:", numerador / denominador)

    elif opcion == "2":
        a = float(input("Introduce a: "))
        b = float(input("Introduce b: "))
        c = float(input("Introduce c: "))
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            print("No hay soluciones reales.")
        else:
            x1 = (-b + math.sqrt(discriminante)) / (2*a)
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            print("Soluciones:", x1, "y", x2)

    elif opcion == "3":
        a = float(input("Introduce a: "))
        b = float(input("Introduce b: "))
        c = float(input("Introduce c: "))
        if b != 0:
            pendiente = -a / b
            ordenada = -c / b
            print("Pendiente:", pendiente)
            print("Ordenada en el origen:", ordenada)
        else:
            if a != 0:
                print("Recta vertical, pendiente indefinida.")
            else:
                print("Recta indefinida.")

    elif opcion == "4":
        n = int(input("Introduce un número natural: "))
        if n <= 0:
            print("El número debe ser natural (>0).")
        else:
            print("Divisores de", n, ":")
            i = 1
            while i <= n:
                if n % i == 0:
                    print(i)
                i += 1

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
