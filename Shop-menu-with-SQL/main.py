import mysql.connector
import MenuAdmins
import Customer
from config import host, user, password, db_name

connection = mysql.connector.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
)

base_shop = connection.cursor()

# base_users.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, login varchar(32), password varchar(32), email varchar(32))") - Добавить таблицу
# base_users.execute("ALTER TABLE users ADD COLUMN название тип данных") - Добавить в таблицу колонну
# base_users.execute("SELECT * FROM users WHERE login ='ЛОГИН'") - Найти в таблице строку по данным


def main():
    do = menu()
    while do != 5:
        connection.commit()
        if do == 1:
            menu_products()
        if do == 2:
            Customer.add_customer()
        if do == 3:
            add_order()
        if do == 4:
            MenuAdmins.edit_products()
        if do not in (1, 2, 3, 4, 5):
            print('Такого пункта нет!')
        do = menu()


def menu_products():  # Просмотр списка товаров
    print('\n\tСписок товаров:')
    db_curs = connection.cursor()
    db_curs.execute("SELECT * FROM products")
    prod_res = db_curs.fetchall()
    for x in prod_res:
        print(f"Позиция: {x[0]}. Название: {x[1]}. Цена: {x[2]}")
    print('\n')


def menu():  # Вызов меню магазина
    print('\n\t\t**Онлайн-магазин вещей для дома**')
    print('Что вы хотите сделать? \n \
              1. Посмотреть список товаров \n \
              2. Регистрация пользователя \n \
              3. Заказать товар \n \
              4. Редактирование товара в каталоге *!Это только для сотрудников!*\n \
              5. Выход')
    do = int(input('Ваш выбор: '))
    return do


def add_order():  # Составить заказ покупателя
    name = input("Введите имя заказчика: ")
    if Customer.auth_customer(name) == 1:
        base_shop.execute(f"SELECT * from customers where name = '{name}'")
        data = base_shop.fetchall()
        print(f'Заказ на адрес: {data[0][1]}. Ваша контактная почта: {data[0][3]}')
        menu_products()
        do = int(input('Меню действий:\n1. Добавить товар\n2. Удалить товар. \n3. Сохранить заказ.\nДействие: '))
        while do != 3:
            if do == 1:
                pass
            if do == 2:
                pass
            if do not in (1,2,3):
                print('Такого пункта нет!')
            do = int(input('Меню действий:\n1. Добавить товар\n2. Удалить товар. \n3. Сохранить заказ.\nДействие: '))
    else:
        do = input("""Такого пользователя нет. 
Хотите зарегистрировать?(yes/no) """)
        if do.lower() == 'yes':
            Customer.add_customer()
        else:
            pass

main()

connection.commit()