import sys
def addition():
     modified_contact = input("Напишите имя!: ")
     modified_contact = modified_contact+" "+input("Напишите телефон: ")
     modified_contact = modified_contact+" "+input("Напишите комментарий: ")+'\n'
     with open("phone_book.txt", 'a') as phone_book_arg:
            phone_book_arg.write(modified_contact)
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
      
      if found_res==0:
           print("Ничего не найдено. =(")
           cursor=input("Выберите действие:\nback - вернуться к списку контактов, find - найти контакт, exit - закрыть справочник")
      elif found_res == 1:
            cursor=input("Выберите действие:\nmodify - изменить данные контакта, delete - удалить контакт, back - для возврата, exit - закрыть справочник")
            while cursor not in ["modify", "delete", "back", "exit"]:
                  print("Error!")
                  cursor = input()
            if cursor == "modify":
                  modify(contact_list,criteria)
            elif cursor == "exit":
                  sys.exit("Good Bye!")
            elif cursor == "back":
                  sys.exit("Good Bye!")
                      
      else:
            cursor=input("Найдено несколько результатов!\nВведите:\nfind и задайте более точные критерии поиска.\nunite - удалить полные копии.\nback - для возврата\nexit - закрыть справочник\n")
            while cursor not in ["find", "unite", "back", "exit"]:
                  print("Error!")
                  cursor = input()      
            if cursor == "unite":
                  find_contact(unite(contact_list))
            elif cursor == "find":
                  find_contact()
            elif cursor == "exit":
                  sys.exit("Good Bye!")


                        
def modify(contact_list_arg, criteria_arg):
    modified_contact = []
    for row in contact_list_arg:
        if criteria_arg in row:
            modified_contact.append(row)
            contact_list_arg.remove(row)
    modified_contact[0] = input("Напишите новое имя!: ")
    modified_contact[1] = input("Напишите новый телефон: ")
    modified_contact[2] = input("Напишите новый комментарий: ")
    contact_list_arg.append(modified_contact)
    print(contact_list_arg)
      
                  
      



                 
                       
def unite(contact_list_arg):
      contact_list_arg=set(map(tuple, contact_list_arg))
      contact_list_arg = [list(line) for line in contact_list_arg]
      return contact_list_arg         


