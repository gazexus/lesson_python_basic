my_list = list(input("enter value: "))
err = my_list.index('#')
del my_list[err]
new_list = ''.join(my_list)
len_letter = max(new_list.split(), key=len)
print(new_list)
print(len_letter)