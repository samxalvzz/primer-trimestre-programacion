def cifrar_mensaje(texto: str) -> str:
    """
    Escribir en Python una funcion llamada cifrar_mensaje(texto) que implemente
    un cifrado tipo <<César>> de forma que cada letra es sustituida por la siguiente
    en el alfabeto (se entiende que la siguiente de la <<z>> es la <<a>>). Los
    caracteres no alfabéticos no deben ser sustituir, y hay que mantener las
    mayusculas y minisculas.
    Indicacion: utilizar las funciones ord() y chr()
    
    >>> cifrar_mensaje('Hola, Mundo!')
    'Ipmb, Nwoep'
    """
    res: list[str] = []
    i = 0
    while i < len(texto):
        c = texto[i]
        if c.isalpha():
            c = chr(ord(c) - 25) if c.lower() == 'z' else chr(ord(c) + 1)
        res.append(c)
        i += 1
    return ''.join(res)
                
                
    
    
    
    
    
    
    
    
    
    
    
    """
    while i < len(texto):
        c = texto[i]
    
    if 'a' <= c <= 'z':
        if c == 'z':
            res += 'a'
        else:
            res += chr(ord(ch) + 1)
        
    elif 'A' <= c <= 'Z':
        if c == 'Z':
            res += 'A'
        else:
            res += chr(ord(ch) + 1)
    else:
        res += c
    i += 1
    return res
    """