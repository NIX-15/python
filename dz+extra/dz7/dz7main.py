import functions_phonebook
phone_book = "phone_book.txt"
#pointer = ""

def check_phone_book(phone_book_arg):
    import os
    if os.path.exists(phone_book_arg) and os.path.getsize(phone_book_arg) > 0:
        with open(phone_book_arg, 'r') as book_data:
            for line in book_data:
                print(line)
        print("Выберите действие:\nadd - добавить контакт, find - найти контакт, exit - закрыть справочник")
        cursor = input()
        while(cursor != "add" and cursor != "exit" and cursor != "find"):
            print("Error!")
            cursor=input()
        if cursor == "add":
           functions_phonebook.addition()
           check_phone_book(phone_book)
        elif cursor == "find":
            functions_phonebook.find_contact(phone_book_arg)
            check_phone_book(phone_book)
        else:
            print("Good Bye!")

    else:
        cursor=input("Справочник пуст!\nВыберите действие:\nadd - добавить контакт, exit - закрыть справочник")
        while(cursor != "add" and cursor != "exit"):
            print("Error!")
            cursor=input()
        if cursor == "add":
           functions_phonebook.addition()
           check_phone_book(phone_book)
        else:
            print("Good Bye!")
                



check_phone_book(phone_book)
