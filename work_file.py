ru = ['один', 'два', 'три', 'четыре', 'пять']
f1 = open('data.txt')
f2 = open('data_new.txt', 'w')

i = 0
for line in f1:
    l = line.split(' - ')
    l[0] = ru[i]
    i += 1
    l = ' - '.join(l)
    f2.write(l)

f1.close()
f2.close()

#f1 = open('data.txt')
#f1.read()