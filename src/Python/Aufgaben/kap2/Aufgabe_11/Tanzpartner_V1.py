damen = ("d1", "d2", "d3", "d4",)
herren = ("h1", "h2", "h3", "h4",)
trainer = ("t1",)

anzahlTanzpaare = 0

for i in range(len(damen)):
    for j in range(len(herren)):
        print(damen[i], " mit ", herren[j])
        anzahlTanzpaare += 1
    for j in range(len(trainer)):
        print(damen[i], " mit ", trainer[j])
        anzahlTanzpaare += 1

for i in range(len(herren)):
    for j in range(len(trainer)):
        print(herren[i], " mit ", trainer[j])
        anzahlTanzpaare += 1

print("\nAnzahl der Paare: ", anzahlTanzpaare)
