factorial = lambda n: 1 if n == 0 else \
                      n * factorial(n -1)

resultado = factorial(3)

potencia = lambda a, b: 1 if b == 0 else a * potencia(a, b - 1)

digitos = lambda n: 1 if n < 10 else 1 + digitos(n // 10)

longitud = lambda s: 0 if s == "" else 1 + longitud(s[1:])

fib = lambda n: 0 if n == 0 else \
                1 if n == 1 else \
                fib(n - 1) + fib(n - 2)

#Hanoi

hanoi = lambda a, b, c, n: "" if n == 0 else \
                           hanoi(a, c, b, n - 1) + \
                           "muevo de " + str(a) + " hacia " + str(b) + " un disco; " + \
                           hanoi(c, b, a, n - 1)