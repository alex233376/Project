def count_words(filename):
    """Читает несколько файлов сразу """
    try:
        with open(filename, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        # print(f"Извините но {filename} не существует.")
        pass
    else:
        for line in lines:
            print(line.rstrip())


filenames = ["glava10/cats.txt", "glava10/dogs.txt"]
for filename in filenames:
    count_words(filename)
