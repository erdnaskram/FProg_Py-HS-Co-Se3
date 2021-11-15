
class Kunde:
    __anzahl = 0

    def __init__(self, nr = 0, name = ""):
        self.__nummer = nr
        self.__name = name

    def getNummer(self):
        return self.__nummer

    def getName(self) :
        return self.__name

    def __str__(self) :
        beschr = self.__nummer + ": " + self.__name
        return beschr

    @staticmethod
    def getAnzahl():
        return Kunde.__anzahl


k1 = Kunde(42, "hellmut")
print(k1)
print(k1.getAnzahl())

k2 = Kunde(34, "dunkelmut")
print(k2)
print(k2.getAnzahl())
