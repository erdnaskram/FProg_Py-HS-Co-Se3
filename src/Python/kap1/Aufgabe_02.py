
f = float(input('Geben sie eine Temperatur in Fahrenheit ein:'))

if f < 0 or f > 100:
    print('Falsche Eingabe')
else:
    c = 5 * (f-32) / 9
    print('Das sind %.1f °C' % c)

    # print('Das sind {%.1f}°C'.format(c))

