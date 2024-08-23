import functions_phonebook
phone_book = "phone_book.txt"

def check_phone_book(phone_book_arg):
    import os
    if os.path.exists(phone_book_arg) and os.path.getsize(phone_book_arg) > 0:
        print("\nПрограмма 'Справочник'\n")
        with open(phone_book_arg, 'r') as contacts:
            for line in contacts: print(line)        
        cursor = input("Выберите действие:\nadd - добавить контакт, find - найти контакт, exit - закрыть справочник\n").lower()
        while cursor not in ["add","exit","find"]: cursor=input("Error!\n").lower()    
        if cursor == "add":
           functions_phonebook.addition()
           check_phone_book(phone_book)
        elif cursor == "find":
            functions_phonebook.find_contact()
            check_phone_book(phone_book)
        else:
            print("Good Bye!")
    else:
        cursor=input("Справочник пуст!\nВыберите действие:\nadd - добавить контакт, exit - закрыть справочник").lower()
        while cursor not in ["add","exit"]: cursor=input("Error!\n").lower()
        (functions_phonebook.addition(), check_phone_book(phone_book)) if cursor == "add" else print("Good Bye!")

check_phone_book(phone_book)