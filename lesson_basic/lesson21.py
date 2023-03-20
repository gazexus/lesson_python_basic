my_list = list(input("enter value: "))
new_letter = []
for i in my_list:
    if my_list.count(i) > 2:
        new_letter.append(i)
        #new_letter.index(i)
letter = new_letter[0]
my_list.remove(letter)

print(f'Буква "{letter}" ошибочно повторяется {len(new_letter) - 2} раз(а)')
print(f'Исправленное слово: {"".join(my_list)}' if len(new_letter) == 3 else 'Не могу исправить' )