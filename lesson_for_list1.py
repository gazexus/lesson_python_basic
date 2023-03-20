import random

def printList(l):
    i = 0
    while i <= 100:
        print("%.2f" % l[i - 1], end='')
        if i % 10 == 0:
            print()
        i += 1

my_list = []
i = 0
while i < 100:
    my_list.append(random.random())
    i += 1
printList(my_list)
my_list.sort()
printList(my_list)