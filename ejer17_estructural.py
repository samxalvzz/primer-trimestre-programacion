"""
17. Escribir un programa que lea un carácter, correspondiente a un dígito hexadecimal:
0, 1, ..., 9, A, B, ..., F
y lo convierta en el valor decimal correspondiente:
0, 1, ..., 9, 10, 11, ..., 15
"""

hexa = input("Introduce un digito hexadecimal (0-9, A-F): ").upper()

if hex_char in "0123456789ABCDEF":
    decimal = int(hex_char, 16)
    print("El valor decimal es:", decimal)
else:
    print("Carácter no válido.")