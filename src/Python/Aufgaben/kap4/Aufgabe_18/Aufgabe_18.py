class SparesVector:
    def __init__(self):
        self.__vec = {}

    def __getitem__(self, key):
        try:
            v = self.__vec[key]
        except:
            return 0.0
        else:
            return v

    def __setitem__(self, key, value):
        self.__vec[key] = float(value)


s = SparesVector()

s[17] = 3.14
s[34] = 8.09
s[234] = 343.1

print("s[17]", s[17])
print("s[34]", s[34])
print("s[234]", s[234])
