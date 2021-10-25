
li = list()

for i in range(5):
    z = int(input('Geben sie {}. Zahl ein:'.format(i+1)))
    li.append(z)

li.sort()

print('Median: ', li[2])