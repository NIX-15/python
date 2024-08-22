def addition():
     new_contact = input("Напишите имя!: ")
     new_contact = new_contact+" "+input("Напишите телефон: ")
     new_contact = new_contact+" "+input("Напишите комментарий: ")+'\n'
     with open("phone_book.txt", 'a') as phone_book_arg:
            phone_book_arg.write(new_contact)
def find_contact(argument = None):
      if argument is None:
            with open("phone_book.txt", 'r') as phone_book_arg:
                  contact_list = [line.split() for line in phone_book_arg]
                  print(contact_list)
      else:
            contact_list = argument
      criteria = input("Напишите Имя/Номер/Комментарий: ")
      found_res = 0
      for line in contact_list:
            for element in line:
                  if element == criteria:
                        found_res+=1
                        print(line)
      # else:
      #       for line in argument:
      #             for element in line:
      #                   if element == criteria:
      #                         found_res+=1
      #                         print(line)
      if found_res==0:
           print("Ничего не найдено. =(")
           cursor=input("Выберите действие:\nback - вернуться к списку контактов, find - найти контакт, exit - закрыть справочник")
      elif found_res == 1:
          cursor=input("Выберите действие:\nmodify - изменить данные контакта, delete - удалить контакт, exit - закрыть справочник")
      else:
           cursor=input("Найдено несколько результатов!\nВведите:\nfind и задайте более точные критерии поиска.\nback - для возврата\nexit - закрыть справочник\n")
           if cursor == "unite":
                 #unite(contact_list)
                 find_contact(unite(contact_list))
                 
                       
def unite(contact_list_arg):
      contact_list_arg=set(map(tuple, contact_list_arg))
      contact_list_arg = [list(line) for line in contact_list_arg]
      print(contact_list_arg)
      return contact_list_arg         


