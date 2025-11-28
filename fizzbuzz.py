"""
Crea una función que tome un número como argumento y devuelva "Fizz", "Buzz"o"FizzBuzz"

Si el número es múltiplo de 3, la salida debe ser "Fizz".
Si el número dado es múltiplo de 5, la salida debe ser "Buzz".
Si el número dado es un múltiplo de 3 y de 5, la salida debe ser "FizzBuzz".
Si el número no es múltiplo de 3 o 5, el número debe mostrarse solo como se muestra en los ejemplos siguientes.
La salida siempre debe ser una cadena incluso si no es un múltiplo de 3 o 5.

Ejemplos
fizz_buzz(3) ➞ "Fizz"

fizz_buzz(5) ➞ "Buzz"

fizz_buzz(15) ➞ "FizzBuzz"

fizz_buzz(4) ➞ "4"
"""

def fizz_buzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
    
print ('Hola' + 'Mundo')

