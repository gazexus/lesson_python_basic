n = int(input('enter value: '))
seconds = n % (24 * 3600)
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(hours)
print(minutes)
print(seconds)