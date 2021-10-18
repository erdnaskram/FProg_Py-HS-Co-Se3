import math

r = float(input('geben sie einen Radius ein'))

o = 4.0 * math.pi * r**2
v = 4.0/3 * math.pi * r**3

print('Radius:', r, 'Oberfläche:', round(o, 2), 'Volumen:', round(v, 2))