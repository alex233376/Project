while True:
    user_name = input("\nEnter name ")
    print('Hello', user_name)

    filename = 'D:/Project/glava10/guest_book.txt'
    with open(filename, 'a', encoding='utf-8') as file_object:
        file_object.write(user_name)
        file_object.write(' Hello\n')
