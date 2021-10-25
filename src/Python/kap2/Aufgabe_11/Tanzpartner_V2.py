damen = set(["d1", "d2", "d3", "d4"])
herren = set(["h1", "h2", "h3", "h4"])
trainer = set(["t1"])

tanzpaare = set(tuple((d, h))
                for d in damen | trainer
                for h in herren | trainer
                if d != h)

print("\nAnzahl der Paare: ", len(tanzpaare))

for p in tanzpaare:
    print(p, end=" ")
