def getDaysPerMonth(month,year):
    dayList = (31,28,31,30,31,30,31,31,30,31,30,31)
    if(month == 2 and year % 4 == 0):
        return 29
    else:
        return dayList[month-1]


print('welcome to the daynumber-Calc')

date = input('choose a date (tt.mm.yyyy) :')
dateLi = date.split('.')

day = int(dateLi[0])
month = int(dateLi[1])
year = int(dateLi[2])

nthDay = day
print(nthDay)
month = month - 1

if(month > 0):
    for x in range(month):
        nthDay = nthDay + getDaysPerMonth(month,year)
        print(nthDay)
        month = month - 1

print('it is day number ', nthDay)