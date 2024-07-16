phone_book = "phone_book.txt"

def check_phone_book_empty(file_name):
    import os
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r') as book_data:
            for line in book_data:
                print(line)
    else:
        print("Справочник пуст")

check_phone_book_empty(phone_book)
