
class Ding:
    _dichte = {'Au': ('Gold', 19.32),
               'Fe': ('Eisen', 7.87),
               'Ag': ('Silber', 10.5)}

    def __init__(self, symbol, volumen):
        self.__volumen = float(volumen)
        self._symbol = symbol

    def getMasse(self):
        return self.__volumen * self._dichte[self._symbol][1]

    def getVolumen(self):
        return self.__volumen

    def __str__(self):
        beschreibung = 'Ein Ding aus' + \
            self._dichte[self._symbol][0] + \
            format(self.getMasse(), '2.f') + 'g'
        return beschreibung


krone = Ding('Au', 200)
print('Masse: ', krone.getMasse(), 'g')