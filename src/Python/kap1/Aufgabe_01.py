import math

k = input('geb Kapital ein:')
p = input('geb Zinssatz ein:')
n = int(input('geb Laufzeit in J ein:'))

k = float(k)
p = float(p)

r = math.pow(k * (1 + p / 100), n)

print('r ist: ', r)