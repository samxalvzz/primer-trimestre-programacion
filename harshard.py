"""
es_harshad(171)
True
es_harshad(481)
True
"""

def es_harshad(n: int) -> bool:
    suma = 0
    m = str(n)
    i = 0
    while i < len(m):
        suma += int(m[i])
        i += 1
        return n % suma == 0