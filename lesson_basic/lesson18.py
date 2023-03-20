my_list = input('enter string')
#lst = []
#for i in my_list:
#    if i.isdigit():
#        int(i)
 #       lst.append(int(i))
lst = [int(i) for i in my_list if i.isdigit()]
print(max(lst))
print(min(lst))
print(sum(lst))

