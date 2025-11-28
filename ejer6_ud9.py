"""
6. Escribe un programa que pida el año actual y el de nacimiento del usuario. Debe calcular
su edad, suponiendo que en el año en curso el usuario ya ha cumplido años.
"""

anyo_actual: int = int(input('Introduzca el año actual: '))
anyo_nacimiento: int = int(input('Introduza su año de nacimiento (4 dígitos): '))
edad: int = anyo_actual - anyo_nacimiento
print('Su edad es:', edad, 'años')