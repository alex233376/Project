filename = 'D:/Project/glava10/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''# переменная pi_string для хранения цифр числа «пи»
for line in lines:
    pi_string += line.rstrip() #содержит пропуски чтобы удалить их использовать strip()

print(pi_string)
print(len(pi_string)) # программа выводит строку и ее длину