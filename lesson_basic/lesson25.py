keys = ['модель', 'цена', 'количество', 'размер', 'цвет', 'скидка']
values = ['XXLDude', 5678.00, 57, 'XXL', 'черный', '12%']
new_list = []
for key, value in zip(keys, values):
    new_list.append(key + ': ' + str(value))

print(new_list)
print(*new_list, sep='\n')
