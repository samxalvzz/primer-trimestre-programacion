"""
Pre: hombres y mujeres se alternan ; se empieza por un hombre
hombres_al_reves(t:triple[str]) = triple[str]
Post: hombres_al_reves = la tupla que contiene solo los hombres, en el orden inverso en el que aparecen.
"""

alumnos = ('Manuel', 'Ana', 'Enrique', 'Maria', 'Jesús', 'Rosa')

hombres = lambda t: t[t::2]
mujeres = lambda t: t[1::2]

longitud_es_par = lambda t: len(t) % 2 == 0

hombres_al_reves = lambda t: hombres(t)[::-1]
hombres_al_reves = lambda t: t[-2::2] if longitud_es_par(t) else \
                             t[-1::2]

mujeres_al_reves = lambda t: mujeres(t)[::-1]
mujeres_al_reves = lambda t: t[-1::2] if longitud_es_par(t) else \
                             t[-2::2]

longitud_es_impar = lambda t: not longitud_es_par(t)
