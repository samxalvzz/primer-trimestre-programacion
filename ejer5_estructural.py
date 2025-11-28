"""
5. Escribir un programa que pida al usuario su edad y que imprima el mensaje «¡Qué
joven!» si es menor de 25 años, «No está mal.» si tiene entre 25 y 40 años y «¡Qué
mayor!» si tiene más de 40 años.
"""
edad = int(input("Introduce tu edad: "))

if edad < 25:
    print("¡Qué joven!")
elif 25 <= edad <= 40:
    print("No esta mal.")
else:
    print("¡Qué mayor!")