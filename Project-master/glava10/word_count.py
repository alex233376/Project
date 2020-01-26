def count_words(filename):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        #msg = "Извините это файл " + filename + " не существует "
        #print(msg)
    else:
        # Подсчет приблизительного количества строк в файле.
        words = contents.split()
        num_words = len(words)
        print("Этот файл " + filename + " содержит " + str(num_words) + " слов ")
filenames = ['glava10/alice.txt', 'glava10/siddhartha.txt', 'glava10/moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
