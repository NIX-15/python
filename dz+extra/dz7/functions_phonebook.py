def addition():
     new_contact = input("Напишите имя!: ")
     new_contact = new_contact+" "+input("Напишите телефон: ")
     new_contact = new_contact+" "+input("Напишите комментарий: ")+'\n'
     with open("phone_book.txt", 'a') as phone_book_arg:
            phone_book_arg.write(new_contact)
def find_contact(phone_book_arg):
     with open("phone_book.txt", 'r') as phone_book_arg:
          phone_book_list = [line.split() for line in phone_book_arg]
     print(phone_book_list)
     criteria = input("Напишите Имя/Номер/Комментарий: ")
     found_res = 0
     for line in phone_book_list:
           for element in line:
                 if element == criteria:
                       found_res+=1
                       print(line)
     if found_res==0:
           print("Ничего не найдено. =(")
           cursor=input("Выберите действие:\nback - вернуться к списку контактов, find - найти контакт, exit - закрыть справочник")
     elif found_res == 1:
          cursor=input("Выберите действие:\nmodify - изменить данные контакта, delete - удалить контакт, exit - закрыть справочник")
     else:
           print("Найдено несколько результатов!\nВведите:\nfind и задайте более точные критерии поиска.\nПорядковый номер одного из результатов для дальнейших действий\nunite для удаления всех дубликатов\nback - для возврата\nexit - закрыть справочник")                      
