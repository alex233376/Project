filename = 'glava10/alice.txt'

with open(filename, encoding='utf-8') as f_obj:
    contents = f_obj.read()
#print(contents)
print('Файл содержит искомых слов ' + str(contents.lower().count('best')))