filename = 'D:/Project/glava10/learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C'))# Заменяем Python на С с помощью функции replace
