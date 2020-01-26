filename = 'glava10/alice.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Извините это файл " + filename + " не существует "
    print(msg)
else:
    # Подсчет приблизительного количества строк в файле.
    words = contents.split()
    num_words = len(words)
    print(f"Этот файл {filename} содержит {num_words} слов ")
