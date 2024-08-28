import os
import shutil
import platform

def create_folder():
    folder_name = input("Введите название папки: ")
    try:
        os.makedirs(folder_name)
        print(f"Папка '{folder_name}' создана.")
    except FileExistsError:
        print(f"Папка '{folder_name}' уже существует.")

def delete_file_or_folder():
    name = input("Введите название файла или папки: ")
    if os.path.isdir(name):
        shutil.rmtree(name)
        print(f"Папка '{name}' удалена.")
    elif os.path.isfile(name):
        os.remove(name)
        print(f"Файл '{name}' удален.")
    else:
        print(f"'{name}' не найдено.")

def copy_file_or_folder():
    src = input("Введите название файла или папки для копирования: ")
    dest = input("Введите новое название: ")
    if os.path.isdir(src):
        shutil.copytree(src, dest)
        print(f"Папка '{src}' скопирована в '{dest}'.")
    elif os.path.isfile(src):
        shutil.copy(src, dest)
        print(f"Файл '{src}' скопирован в '{dest}'.")
    else:
        print(f"'{src}' не найдено.")

def view_directory_contents():
    for item in os.listdir():
        print(item)

def view_folders():
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)

def view_files():
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)

def view_os_info():
    print(platform.uname())

def view_creator_info():
    print("Создатель программы: Евгений")

def quiz_game():
    again = 'да'
    while again.lower() == 'да':
        right = 0
        wrong = 0

        query1 = input("Год рождения Ленин В.И.: ")  # год рождения 1870
        if query1 == "1870":
            print("Верно")
            right += 1
        else:
            print("Ошибка")
            wrong += 1

        query2 = input("Год рождения Сталина И.В.: ") # год рождения 1879
        if query2 == "1879":
            print("Верно")
            right += 1
        else:
            print("Ошибка")
            wrong += 1

        query3 = input("Год рождения Брежнева Л.И.: ") # год рождения 1906
        if query3 == "1906":
            print("Верно")
            right += 1
        else:
            print("Ошибка")
            wrong += 1

        query4 = input("Год рождения Ельцин Б.Н.: ") # год рождения 1931
        if query4 == "1931":
            print("Верно")
            right += 1
        else:
            print("Ошибка")
            wrong += 1

        query5 = input("Год рождения Путина В.В.: ") # год рождения 1952
        if query5 == "1952":
            print("Верно")
            right += 1
        else:
            print("Ошибка")
            wrong += 1

        print("Верно", right)
        print("Ошибок", wrong)
        print("Верно", right * 100 / 5, "%")
        print("Ошибок", wrong * 100 / 5, "%")

        again = input("Хотите ли начать игру сначала? ")  # да/нет

def bank_account():
    balance = 0
    purchases = []

    def main_menu():
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

    def top_up_balance(balance):
        amount = float(input('Введите сумму для пополнения счета: '))
        balance += amount
        print(f'Ваш новый баланс: {balance}')
        return balance

    def make_purchase(balance, purchases):
        amount = float(input('Введите сумму покупки: '))
        if amount > balance:
            print('Недостаточно средств на счету')
        else:
            name = input('Введите название покупки: ')
            balance -= amount
            purchases.append((name, amount))
            print(f'Вы купили {name} на сумму {amount}. Ваш новый баланс: {balance}')
        return balance

    def show_purchase_history(purchases):
        if purchases:
            print('История покупок:')
            for name, amount in purchases:
                print(f'{name}: {amount}')
        else:
            print('История покупок пуста')

    while True:
        main_menu()
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            balance = top_up_balance(balance)
        elif choice == '2':
            balance = make_purchase(balance, purchases)
        elif choice == '3':
            show_purchase_history(purchases)
        elif choice == '4':
            print('Выход из программы управления счетом')
            break
        else:
            print('Неверный пункт меню')

def change_working_directory():
    new_path = input("Введите полный или относительный путь: ")
    try:
        os.chdir(new_path)
        print(f"Рабочая директория изменена на '{os.getcwd()}'.")
    except FileNotFoundError:
        print(f"Путь '{new_path}' не найден.")

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            create_folder()
        elif choice == '2':
            delete_file_or_folder()
        elif choice == '3':
            copy_file_or_folder()
        elif choice == '4':
            view_directory_contents()
        elif choice == '5':
            view_folders()
        elif choice == '6':
            view_files()
        elif choice == '7':
            view_os_info()
        elif choice == '8':
            view_creator_info()
        elif choice == '9':
            quiz_game()
        elif choice == '10':
            bank_account()
        elif choice == '11':
            change_working_directory()
        elif choice == '12':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()