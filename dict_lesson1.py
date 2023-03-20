school = {'1a': 10, '1b': 12, '2a': 15, '6a': 12, '7v': 20}
print(school)

school['6a'] = 25
school['8d'] = 15
del school['1b']

sum_student = 0
for i in school.values():
    sum_student += i

print(school)
print(sum_student)