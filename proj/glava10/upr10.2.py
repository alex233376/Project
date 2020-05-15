filename = 'glava10/learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    a = line.rstrip()
    print(a.replace('Python', 'C'))
