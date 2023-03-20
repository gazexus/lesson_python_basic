my_list = input("enter: ").split(' ')
n = []
s = []
w = []
e = []

for i in my_list:
    if i[0] == 'e':
        e.append(int(i[1:]))
    elif i[0] == 'n':
        n.append(int(i[1:]))
    elif i[0] == 's':
        s.append(int(i[1:]))
    elif i[0] == 'w':
        w.append(int(i[1:]))
print(f'x: {sum(e) - sum(w)} y: {sum(n) - sum(s)}')
print(my_list)