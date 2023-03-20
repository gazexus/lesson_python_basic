n = int(input("enter number: "))

my_list = []

for _ in range(n):
    word_ = input("enter word: ").lower()
    my_list.append(word_)


print(''.join(my_list))
print(f" Количество уникальных символов во всех словах:{len(set(''.join(my_list)))}")