
def haeufigkeiten(w):
    strawberryDict = {}
    wordArray = list(w)
    for x in wordArray:
        strawberryDict[x] = w.count(x)
    return strawberryDict


word = input('geben sie ein Wort ein:')
strawberryDict = haeufigkeiten(word)

for key, value in strawberryDict.items():
    print(key, ": ", value)
