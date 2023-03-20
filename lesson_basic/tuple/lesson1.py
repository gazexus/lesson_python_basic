my_tuple = tuple(map(int, input("enter number: ").split()))
#my_tuple = tuple(my_tuple)

posit_list = tuple(i for i in my_tuple if i > 0)
negat_list = tuple(i for i in my_tuple if i < 0)

#for i in my_tuple:
#    if i  > 0:
#        posit_list.append(i)
#    else:
#      negat_list.append(i)

print(f'Кортеж {posit_list} состоит из {len(posit_list)} положительных чисел')
print(f'Кортеж {negat_list} состоит из {len(negat_list)} положительных чисел')

