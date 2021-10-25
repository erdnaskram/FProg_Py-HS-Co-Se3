import copy


def caesar_encode(sntc, dist):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    codetAlphabet = copy.deepcopy(alphabet)
    for i in range(len(alphabet)):
        z = i + dist
        if z > 25:
            z -= 26
        codetAlphabet[i] = alphabet[z]
    for i in range(len(alphabet)):
        alphabet.append(alphabet[i].upper())
        codetAlphabet.append(codetAlphabet[i].upper())

    # sntc = sntc.lower()

    res = ""

    for i in range(len(sntc)):
        if sntc[i] in codetAlphabet:
            res = res + codetAlphabet[alphabet.index(sntc[i])]
        else:
            res = res + sntc[i]

    return res


def caesar_decode(sntc, dist):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    codetAlphabet = copy.deepcopy(alphabet)
    for i in range(len(alphabet)):
        z = i + dist
        if z > 25:
            z -= 26
        codetAlphabet[i] = alphabet[z]

    for i in range(len(alphabet)):
        alphabet.append(alphabet[i].upper())
        codetAlphabet.append(codetAlphabet[i].upper())

    # sntc = sntc.lower()

    res = ""

    for i in range(len(sntc)):
        if sntc[i] in codetAlphabet:
            res = res + alphabet[codetAlphabet.index(sntc[i])]
        else:
            res = res + sntc[i]

    return res
