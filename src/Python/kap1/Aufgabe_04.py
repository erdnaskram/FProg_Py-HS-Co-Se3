
p1 = (-1.1, 3.5)
p2 = (2.4, -0.7)

dx = p2[0] - p1[0]
dy = p2[1] - p1[1]

print('Erster Punkt: P1 = (', p1[0], ',', p1[1])
print('Zweiter Punkt: P2 = (', p2[0], ',', p2[1])

if dx == 0:
    print('Die Gerade durch beide Punkte ist senkrecht bei x = ', dy)
else:
    m = dy / dx
    c = p1[1] - m * p1[0]

    print('Für die Gerade y = mx + c durch P1 und P2 gilt:')
    print('m= ', m, ' und c = ', c)