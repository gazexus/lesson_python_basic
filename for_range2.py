N = 5
word = [''] * N
len_val = [0] * N
for i in range(N):
    word[i] = input()
    len_val[i] = len(word[i])
print(word)
print(len_val)