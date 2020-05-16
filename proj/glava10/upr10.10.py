filename = 'glava10/alice.txt'
with open(filename, encoding='utf -8') as f:
    # readlines() последовательно читает каждую строку из файла
    lines = f.read()
    line = lines.lower().count('alice')  # Считаем количество вхождений alice
    print(line)  # выводятся все элементы списка lines
