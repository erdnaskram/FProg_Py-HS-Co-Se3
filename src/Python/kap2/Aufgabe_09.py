print('welcome to the weekday-Calc')

date = input('choose a date (tt.mm.yyyy) :')
dateLi = date.split('.')

weekDays = ['Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag']
day = int(dateLi[0])
month = int(dateLi[1])
year = int(dateLi[2])
h = year//100
j = year-h*100

w = (day + (month+1)*26//10 + 5*j//4 + h//4 - 2*h - 1) % 7

print('the weekday is: ',weekDays[w-1])