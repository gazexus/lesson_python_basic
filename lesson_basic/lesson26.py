my_list = input("enter: ").split(',')
new_list = []
print(my_list)
for i in my_list[1].split():
    new_list.append(int(i))

mid_bal = sum(new_list) / len(new_list)
print(f'{my_list[0]}, средний балл: {mid_bal:.2f}')
