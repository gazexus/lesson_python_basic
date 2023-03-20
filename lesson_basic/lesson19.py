my_list = input().split()
st = []
for i in my_list:
    st.append(int(i))
print(st)
lst = []
for i in st:
    if st.count(i) > 1:
        lst.append(i)
print(*lst)

