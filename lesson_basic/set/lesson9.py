n = int(input("enter value: "))
my_list = []
for _ in range(n):
    color_ = input("enetr color: ").lower()
    my_list.append(color_)

if len(my_list) > len(set(my_list)):
    print("повтор")
else:
    print("принято")
print(my_list)
