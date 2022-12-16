import view

phone_book = []

def get_phone_book () -> list:
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    new_contact = view.input_new_contact()
    phone_book.append(new_contact)
    print(f'Контакт {new_contact[0]} добавлен')

def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно хотите удалить контакт {phone_book[id-1][0]} (y/n)')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id-1)
        print(f'Контакт {del_contact} удален')

def find_contact():
    global phone_book
    find_string = view.input_find()
    for id, contact in enumerate(phone_book):
        for item in contact:
            if find_string in item.lower():
                return id, contact
            else:
                print('По вашему запросу ничего не найдено')
