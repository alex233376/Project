filename = 'glava10/alice.txt'
try:
    with open(filename, encoding='utf -8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Извините но файла {filename} не существует ")
else:
    # Подсчет приблизительного количества строк в файле.
    words = contents.split()
    num_words = len(words)
    print(f"Этот файл {filename} содержит {num_words} слов ")
