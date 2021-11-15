from os import walk
from os.path import normcase, join, getmtime
from time import time, ctime


def dateisuche(start, zeit):
    tree = walk(start)
    result = []
    limit = time() - zeit * 3600

    for pfad, verz, dateien in tree:
        for datei in dateien:
            # print("Pfad", pfad, "Datei:", datei)
            try:
                dateipfad = normcase(join(pfad, datei))
                dateizeit = getmtime(dateipfad)
                if dateizeit > limit:
                    result.append(dateizeit, dateipfad)
            except FileNotFoundError:
                continue
    print("Datei und Zeitpunkt letzter Änderung:")
    for t, pfad in result:
        print("{} {}".format(pfad, ctime(t)))


start = input("Wurzel des Verzeichnisses")
