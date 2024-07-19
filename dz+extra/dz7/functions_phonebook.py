def addition():
     new_contact = input("Напишите имя!: ")
     new_contact = new_contact+" "+input("Напишите телефон: ")
     new_contact = new_contact+" "+input("Напишите комментарий: ")+'\n'
     with open("phone_book.txt", 'a') as book_data:
            book_data.write(new_contact)
def find_contact(file_name):
     with open("phone_book.txt", 'r') as book_data:
          print(len(book_data.readlines()))
     criteria = input("Напишите Имя/Номер/Комментарий: ")