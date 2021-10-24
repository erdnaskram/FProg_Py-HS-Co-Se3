import CesarCode

toDecode = 'Ugpco ypvi xb zdbeatii ktglpwgadhitc Ipmx fjtg sjgrw Qpntgc.'

for k in range(25):
    # Dist 15 ist die lösung
    print('Dist:',k)
    print(CesarCode.caesar_decode(toDecode,k))

print("\nVerschlüsselt:")
print(CesarCode.caesar_encode("franz jagt im komplett verwahrlosten taxi quer durch bayern.",15))