filename = 'glava10/learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())  # rstrip() убирает пробелы
