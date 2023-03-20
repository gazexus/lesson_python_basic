word1, word2 = input("enter word1: ").lower(), input("enter word2: ").lower()

dict_word1 = {}
dict_word2 = {}

for i in word1:
    dict_word1[i] = word1.count(i)
for i in word2:
    dict_word2[i] = word2.count(i)
print(dict_word1)
print(dict_word2)
print('Yes' if dict_word1 == dict_word2 else 'No')
