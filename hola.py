# 1. Escribe una función que tome la base y la altura de un triángulo y return su área.
def tri_area(base, altura):
    return (base * altura) / 2

# 2. Crea una función que encuentre el rango máximo del tercer borde de un triángulo, 
# donde las longitudes de los lados son todos números enteros.
def next_edge(lado1, lado2):
    return (lado1 + lado2) - 1

# 3. Crea una función que tome el largo y el ancho encuentre el perímetro de un rectángulo.
def encontrar_perímetro(largo, ancho):
    return 2 * (largo + ancho)

# 4. Crea una función que toma voltaje y la corriente eléctrica y que devuelva la potencia calculada.
def potencia_calculada(voltaje, corriente_eléctrica):
    return voltaje * corriente_eléctrica

# 5. Crea una función que tome un número base y un número exponente y devuelva el cálculo.
def calcular_exponente(número, exponente):
    return número ** exponente

# 6. Corrija el código en la pestaña de código para superar este desafío (solo errores de sintaxis). 
# Observe los ejemplos a continuación para tener una idea de lo que debería hacer la función.
def al_cuadrado(b):
    return b * b

# 7. Un estudiante que estaba aprendiendo Python intentaba crear una función. Su código debía concatenar una cadena pasada namecon una cadena "Edabit" 
# y almacenarla en una variable llamada result. Necesita tu ayuda para corregir este código.
def name_string(nombre):
    b = "Edabit"
    resultado = nombre + b
    return resultado

# 8. Escriba una función que tome dos números enteros ( hours, minutes), los convierta en segundos y los sume.
def convertir(horas, minutos):
    return horas * 3600 + minutos * 60

# 9. Escribe dos funciones:
# to_int():Una función para convertir una cadena en un entero.
# to_str():Una función para convertir un entero en una cadena.
def to_int(txt):
    return int(txt)
def to_str(num):
    return str(num)

# 10. Usted está contando puntos para un juego de baloncesto, dada la cantidad de 3-punteros anotados y 2-punteros anotados, encuentre los puntos finales para el equipo 
# y devuelva ese valor ([2 -punteros anotados, 3-punteros anotados]).
def puntos(dospuntos_anotados, trespuntos_anotados):
    return dospuntos_anotados * 2 + trespuntos_anotados * 3

# 11. Crea una función que retorna Truecuando num1es igual a num2; de lo contrario, retorna False.
def es_el_mismo_num(num1, num2):
    return num1 == num2

#12. Crea una función que tome una lista de números. Devuelve el número más grande de la lista.
def listanumeros(nums):
    return max(listanumeros)
"Con esto comprobaremos bien que se puede hacer o no"
print(listanumeros([3, 5, 7, 9, 11, 2, 4]))

#13. Crea una función que tome una lista de números y devuelva el número más pequeño de la lista.
def listanumeros(nums):
    return min(listanumeros)
"Con esto comprobaremos bien que se puede hacer o no"
print(listanumeros([3, 5, 7, 9, 11, 2, 4]))

#14. Crea una función para concatenar dos listas de enteros.
def concatenar(lista1, lista2):
    return lista1 + lista2
"Vamos a comprobar con un print"
print(concatenar([1, 2, 3], [4, 5, 6]))

#15. Crea una función que acepte una lista y devuelva el último elemento. La lista puede ser homogénea o heterogénea.
def obtener_último_elemento(lista):
    return lista[-1]
