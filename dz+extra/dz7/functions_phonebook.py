import sys
def addition():
     new_contact_name = input("Напишите имя!: ").capitalize()
     new_contact_number = input("Напишите телефон: ")
     while not new_contact_number.isdigit() or len(new_contact_number) > 11:
            new_contact_number = input("Ошибка! Номер должен состоять из цифр и не более 11 символов!\n")
     new_contact = new_contact_name+" "+new_contact_number+" "+input("Напишите комментарий: ")+'\n'
     with open("phone_book.txt", 'a') as phone_book_arg:
            phone_book_arg.write(new_contact)
def find_contact(argument = None):
      if argument is None:
            with open("phone_book.txt", 'r') as phone_book_arg:
                  contact_list = [line.split() for line in phone_book_arg]
                  for contact in contact_list:
                        print(" ".join(contact))
      else:
            contact_list = argument
      criteria = input("Напишите Имя/Номер/Комментарий: ")
      found_res = 0
      for line in contact_list:
            for element in line:
                  if element.lower() == criteria.lower():
                        found_res+=1
                        print(" ".join(line))
      
      if found_res==0:
            print("Ничего не найдено. =(")
            cursor=input("Выберите действие:\nback - вернуться к списку контактов, \
find - найти контакт, exit - закрыть справочник\n").lower()
            while cursor not in ["find","back","exit"]: cursor = input("Error!\n").lower()      
            if cursor == "find": find_contact()
            elif cursor == "exit": sys.exit("Good Bye!")

      elif found_res == 1:
            cursor=input("Выберите действие:\nmodify - изменить данные контакта, delete - удалить контакт, \
back - для возврата, exit - закрыть справочник\n").lower()
            while cursor not in ["modify", "delete", "back", "exit"]: cursor = input("Error!\n").lower()
            if cursor == "modify": modify_contact(contact_list,criteria)
            elif cursor == "exit": sys.exit("Good Bye!")
            elif cursor == "delete": delete_contact(contact_list,criteria)
                      
      else:
            cursor=input("Найдено несколько результатов!\nВведите:\nfind и задайте более точные критерии поиска.\
\nunite - удалить полные копии.\nback - для возврата\nexit - закрыть справочник\n").lower()
            while cursor not in ["find", "unite", "back", "exit"]: cursor = input("Error!\n").lower()                        
            if cursor == "unite": find_contact(unite_copies(contact_list))
            elif cursor == "find": find_contact()
            elif cursor == "exit": sys.exit("Good Bye!")

def write_result(contact_list_arg):
    with open('phone_book.txt', 'w') as phone_book:
        for row in contact_list_arg:
            row[0] = row[0].capitalize()
            phone_book.write(' '.join(str(elem) for elem in row) + '\n')
                        
def modify_contact(contact_list_arg, criteria_arg):
      for row in range(len(contact_list_arg)):
            if criteria_arg.lower() in [element.lower() for element in contact_list_arg[row]]:                
                  contact_list_arg[row][0] = input("Напишите новое имя!: ").capitalize()
                  contact_list_arg[row][1] = input("Напишите новый телефон: ")
                  while not contact_list_arg[row][1].isdigit() or len(contact_list_arg[row][1]) > 11:
                        contact_list_arg[row][1] = input("Ошибка! Номер должен состоять из цифр и не более 11 символов!\n")
                  contact_list_arg[row][2] = input("Напишите новый комментарий: ")
                  print(f"Изменения для контакта {(" ".join(contact_list_arg[row][0]))} внесены!")
                  write_result(contact_list_arg)


def delete_contact(contact_list_arg, criteria_arg):
      for row in contact_list_arg:
            if criteria_arg.lower() in [element.lower() for element in row]:
                  comfirm_delete = input(f"Контакт {(", ".join(row))} будет удалён. Подтвердить? (Введите yes или no)\n")
                  while comfirm_delete.lower() not in ["yes","no"]:
                        comfirm_delete=input("Error!\n")
                  if comfirm_delete.lower() == "yes":
                        contact_list_arg.remove(row)
                        write_result(contact_list_arg)
     
def unite_copies(contact_list_arg):
      contact_list_arg=set(map(tuple, contact_list_arg))#Списки не хэшируются, нужно сперва переводить в кортежи
      contact_list_arg = [list(line) for line in contact_list_arg]
      print("Копии контактов удалены!")
      write_result(contact_list_arg)
      return contact_list_arg         