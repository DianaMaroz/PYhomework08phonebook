import phone_book as pb


def main_menu():
    print('Выберите команду меню')
    print('1. Показать телефонную книгу')
    print('2. Загрузить телефонную книгу')
    print('3. Сохранить телефонную книгу')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выйти из приложения \n')
    return input_menu()

def input_menu():
    while True:
        try:
            choice = int(input(' Введите пункт меню: '))
            if choice in range(1, 8) or choice == 0:
                return choice
            else:
                print('Такого пункта нет в меню. Внимательнее, пожалуйста: ')
        except:
            print('Ошибка ввода. Введите корректный пункт меню:  ')


def print_phone_book():
    phone_book = pb.get_phone_book()
    print()
    if len(phone_book) < 1:
        print('Телефонная книга пуста или не загружена \n')
    else:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    print()

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий контакта: ')
    new_contact = [name, phone, comment]
    return new_contact

def input_remove_contact():
    print()
    print_phone_book()
    id = int(input('Введите ID контакта, который хотите удалить: '))
    return id

def input_find():
    print('Поиск не чувствителен к регистру.')
    find = input('Введите строку для поиска: ').lower()
    return find


def input_change_contact():
    print()
    print_phone_book()
    id = int(input('Введите ID контакта, который хотите изменить: '))
    return id

def change_menu():
    print('Выберите команду ')
    print('1. Если хотите изменить имя')
    print('2. Если хотите изменить номер')
    print('3. Если хотите изменить комментарий')
    print('4. Если хотите изменить контакт полностью')
    print('0. Выйти \n')
    return input_menu()