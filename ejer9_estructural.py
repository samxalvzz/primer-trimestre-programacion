"""
9. Escribir un programa que guarde en una lista diez cadenas introducidas por teclado y
luego las muestre en orden inverso a como se han introducido, desde la última cadena
introducida hasta la primera.
"""
lista = []

print("Introduce 10 cadenas de texto")

i = 0
while i < 10:
    c = input(f"Cadena {i+1}: ")
    lista.append(c)
    i += 1

print("\nCadenas en orden inverso: ")
j = 9
while j >= 0:
    print(lista[j])
    j -= 1