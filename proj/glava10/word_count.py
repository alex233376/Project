def count_words(filename):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(filename, encoding='utf -8') as f:
            contents = f.read()

    except FileNotFoundError:
        # print(f"Извините но файла {filename} не существует ")
        pass
    else:

        words = contents.split()
        num_words = len(words)
        print(f"Этот файл {filename} содержит {num_words} слов ")


filenames = ['glava10/alice.txt', 'glava10/siddhartha.txt',
             'glava10/moby_dick.txt', 'glava10/little_women.txt']
for filename in filenames:
    count_words(filename)
