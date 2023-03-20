my_tuple = (('красный', 33, 55), ('зеленый', 17, 44), ('синий', 12, 3), ('черный', 2, 5))
sort_tuple = tuple(sorted(list(my_tuple), key=lambda x: x[2]))

print(sort_tuple)