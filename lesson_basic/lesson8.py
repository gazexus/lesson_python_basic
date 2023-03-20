string = 'Python лучше всего подходит для новичков.'
print(string.replace(' ', ','))
print(string.split())
print(string.partition('всего'))
text = 'abracadabra123456'
print(text.isalnum())
text1 = 'abracadab23ra'
print(text1.isalpha())
text2 = '123456789w0'
print(text2.isdigit())

text3 = 'пример текста, в котором нужно найти текстовую подстроку'
print(text3.find('текст'))