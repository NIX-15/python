
phone_book = "phone_book.txt"
pointer = ""
def addition():
     new_contact = input("Напишите имя!: ")
     new_contact = new_contact+input("Напишите телефон: ")
     new_contact = new_contact+input("Напишите комментарий: ")
     with open("phone_book.txt", 'a') as book_data:
            book_data.write(new_contact)
def check_phone_book_empty(file_name,cursor):
    import os
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r') as book_data:
            for line in book_data:
                print(line)
    else:
        print("Справочник пуст!")
        print("Выберите действие:\nadd - добавить контакт, exit - закрыть справочник")
        cursor=input()
        while(cursor != "add" and cursor != "exit"):
            print("Error!")
            cursor=input()
        if(cursor == "add"):
           addition()
           check_phone_book_empty(phone_book,pointer)
        else:
            print("Good Bye!")
                



check_phone_book_empty(phone_book,pointer)
