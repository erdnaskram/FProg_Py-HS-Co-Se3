import math

k = float(input('geb Kapital ein:'))
p = float(input('geb Zinssatz ein:'))
n = int(input('geb Laufzeit in J ein:'))

r = math.pow(k * (1 + p / 100), n)

print('r ist: ', r)