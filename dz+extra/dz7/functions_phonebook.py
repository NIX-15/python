import sys
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
      
      if found_res==0:
            print("Ничего не найдено. =(")
            cursor=input("Выберите действие:\nback - вернуться к списку контактов, find - найти контакт, exit - закрыть справочник\n")
            while cursor not in ["find","back","exit"]:
                  cursor = input("\nError!\n")      
            if cursor == "find":
                  find_contact()
            elif cursor == "exit":
                  sys.exit("Good Bye!")

      elif found_res == 1:
            cursor=input("Выберите действие:\nmodify - изменить данные контакта, delete - удалить контакт, back - для возврата, exit - закрыть справочник\n")
            while cursor not in ["modify", "delete", "back", "exit"]:
                  print("Error!")
                  cursor = input()
            if cursor == "modify":
                  modify_contact(contact_list,criteria)
            elif cursor == "exit":
                  sys.exit("Good Bye!")
            elif cursor == "delete":
                  delete_contact(contact_list,criteria)
                      
      else:
            cursor=input("Найдено несколько результатов!\nВведите:\nfind и задайте более точные критерии поиска.\nunite - удалить полные копии.\nback - для возврата\nexit - закрыть справочник\n")
            while cursor not in ["find", "unite", "back", "exit"]:
                  print("Error!")
                  cursor = input()      
            if cursor == "unite":
                  find_contact(unite_copies(contact_list))
            elif cursor == "find":
                  find_contact()
            elif cursor == "exit":
                  sys.exit("Good Bye!")

def write_result(contact_list_arg):
    with open('phone_book.txt', 'w') as phone_book:
        for row in contact_list_arg:
            phone_book.write(' '.join(str(elem) for elem in row) + '\n')
                        
def modify_contact(contact_list_arg, criteria_arg):
      for row in range(len(contact_list_arg)):
            if criteria_arg in contact_list_arg[row]:                
                  contact_list_arg[row][0] = input("Напишите новое имя!: ")
                  contact_list_arg[row][1] = input("Напишите новый телефон: ")
                  contact_list_arg[row][2] = input("Напишите новый комментарий: ")
                  print(f"Изменения для контакта {contact_list_arg[row][0]} внесены!")
                  write_result(contact_list_arg)


def delete_contact(contact_list_arg, criteria_arg):
      for row in contact_list_arg:
            if criteria_arg in row:
                  comfirm_delete= input(f"Контакт {row} будет удалён. Подтвердить? (Введите yes или no)\n")
                  while comfirm_delete not in ["yes","no"]:
                        comfirm_delete=input("Error!\n")
                  if comfirm_delete == "yes":
                        contact_list_arg.remove(row)
                        write_result(contact_list_arg)

                       
def unite_copies(contact_list_arg):
      contact_list_arg=set(map(tuple, contact_list_arg))#Списки не хэшируются, нужно сперва переводить в кортежи
      contact_list_arg = [list(line) for line in contact_list_arg]
      print("Копии контактов удалены!")
      return contact_list_arg         
