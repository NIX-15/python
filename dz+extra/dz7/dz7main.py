import functions_phonebook
phone_book = "phone_book.txt"
pointer = ""

def check_phone_book(file_name,cursor):
    import os
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r') as book_data:
            for line in book_data:
                print(line)
        print("Выберите действие:\nadd - добавить контакт, find - найти контакт, exit - закрыть справочник")
        cursor = input()
        while(cursor != "add" and cursor != "exit" and cursor != "find"):
            print("Error!")
            cursor=input()
        if cursor == "add":
           functions_phonebook.addition()
           check_phone_book(phone_book,pointer)
        elif cursor == "find":
            functions_phonebook.find_contact(file_name)
            check_phone_book(phone_book,pointer)
        else:
            print("Good Bye!")

    else:
        print("Справочник пуст!\nВыберите действие:\nadd - добавить контакт, exit - закрыть справочник")
        cursor=input()
        while(cursor != "add" and cursor != "exit"):
            print("Error!")
            cursor=input()
        if cursor == "add":
           functions_phonebook.addition()
           check_phone_book(phone_book,pointer)
        else:
            print("Good Bye!")
                



check_phone_book(phone_book,pointer)
