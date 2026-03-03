import mysql.connector
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


def auth_products():  # Авторизация в меню редактирования товаров
    print('Это меню только для сотрудников.')
    adm_pass = input('Введите пароль: ')
    count = 1
    while adm_pass != '123adm' and count != 3:
        print(f'Пароль неправильный. Осталось попыток: {3-count} ')
        adm_pass = input('Введите пароль: ')
        count += 1
    if count == 3:
        print('Вы использовали все попытки входа')
        return 0
    if adm_pass == '123adm':
        return 1


def add_product():  # Добавить товар
    sql = "INSERT INTO products (product,cost) values (%s, %s)"
    product = input('Название товара: ')
    base_shop.execute(f"SELECT * from products where product = '{product}'")
    data = base_shop.fetchall()
    print(data)
    if data == []:
        cost = int(input('Цена товара: '))
        products = (product, cost)
        base_shop.execute(sql, products)
        connection.commit()
    else:
        print('Товар уже существует. Добавить такой же невозможно')
        edit_products()


def edit_product():
    pass


def delete_product():  # Удалить товар
    id_product = (input('Введите id товара: '))
    base_shop.execute(f"SELECT * from products where id = {id_product}")
    data = base_shop.fetchall()
    if data != []:
        base_shop.execute(f"DELETE FROM products WHERE id = {id_product}")
        print('Товар удалён.')
    else:
        print('Такого товара нет.')
        edit_products()


def edit_menu():  # Меню редактирования товара
    print('\tВыберите вид работы с товаром:\n \
                        1. Добавить товар. \n \
                        2. Редактировать товар.\n \
                        3. Удалить товар \n \
                        4. Посмотреть список товаров. \n \
                        5. Выйти из меню')
    do = int(input('Ваш выбор: '))
    return do


def edit_products():  # Редактирование товаров
    if auth_products():
        do = edit_menu()
        while do != 5:
            connection.commit()
            if do == 1:
                add_product()
            if do == 2:
                pass
            if do == 3:
                delete_product()
            if do == 4:
                menu_products()
            if do not in (1, 2, 3, 4, 5):
                print('Такого пункта нет!')
            do = edit_menu()
    else:
        pass


def auth_customer(name):  # Проверка есть ли пользователь
    base_shop.execute(f"SELECT * from customers where name = '{name}'")
    data = base_shop.fetchall()
    if data:
        return 1
    else:
        return 0


def add_customer():  # Зарегистрировать пользователя
    sql = "INSERT INTO customers (name,address,email) values (%s, %s, %s)"
    name = input("Введите ваше имя (Пример - John Langford): ")
    if auth_customer(name) == 0:
        address = input("Введите ваш адрес (Пример - Bigfoot st 13): ")
        email = input("Введите ваш email: ")
        customer = (name, address, email)
        base_shop.execute(sql, customer)
        print('Вы зарегистрировались!')
    else:
        print('Пользователь уже зарегистрирован!')


def add_order():  # Составить заказ покупателя
    pass


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


def main():
    do = menu()
    while do != 5:
        connection.commit()
        if do == 1:
            menu_products()
        if do == 2:
            add_customer()
        if do == 3:
            print('Рано ещо')
        if do == 4:
            edit_products()
        if do not in (1, 2, 3, 4, 5):
            print('Такого пункта нет!')
        do = menu()



main()

connection.commit()