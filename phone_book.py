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
    not_find = True
    for id, contact in enumerate(phone_book):
        for item in contact:
            if find_string in item.lower():
                not_find = False
                print((id + 1), *contact)
    if not_find:
        print('По вашему запросу ничего не удалось найти')

def change_menu(change, id):
    global phone_book
    match change:
        case 1:
            phone_book[id-1][0] = input('Введите новое имя контакта:  ')
        case 2:
            phone_book[id - 1][1] = input('Введите новый телефон контакта:  ')
        case 3:
            phone_book[id - 1][2] = input('Введите новый телефон контакта:  ')
        case 4:
            phone_book[id - 1] = view.input_new_contact()
        case 0:
            return True


def change_contact():
    global phone_book
    id = view.input_change_contact()
    print(*phone_book[id-1])
    confirm = input(f'Вы точно хотите изменить контакт {phone_book[id - 1][0]} (y/n)')
    if confirm.lower() == 'y':
        while True:
            change = view.change_menu()
            if change_menu(change, id):
                break
        print('Контакт был изменен: ', end='')
        print(*phone_book[id-1])

