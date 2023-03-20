my_book1 = set(input("enter name book1: ").lower().split(', '))
my_book2 = set(input("enter name book2: ").lower().split(', '))

print(my_book1)
print(my_book2)

sum_book = len(my_book1.intersection(my_book2))
print(f'прочитали оба ученика {sum_book}')




