my_list = []
i = 0
while i < 8:
    my_list.append(float(input("enter 8 value: ")))
    i += 1

print("Min value: ", min(my_list))
print("Max value: ", max(my_list))
print("Sum : ", sum(my_list))