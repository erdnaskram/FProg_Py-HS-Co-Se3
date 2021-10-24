import math

def umfangKreis(radius):
    return round(2 * radius * math.pi,2)

def flaecheKreis(radius):
    return round(math.pi * math.pow(radius,2),2)

def summeUmfangKreis(radiusliste):
    res = 0
    for i in range(len(radiusliste)):
        res += umfangKreis(radiusliste[i])
    return round(res,2)

def summeFlaecheKreis(radiusliste):
    res = 0
    for i in range(len(radiusliste)):
        res += flaecheKreis(radiusliste[i])
    return round(res,2)
