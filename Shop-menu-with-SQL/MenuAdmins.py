import mysql
from config import host, user, password, db_name

connection = mysql.connector.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
)

base_shop = connection.cursor()


def menu_products():  # Просмотр списка товаров
    print('\n\tСписок товаров:')
    db_curs = connection.cursor()
    db_curs.execute("SELECT * FROM products")
    prod_res = db_curs.fetchall()
    for x in prod_res:
        print(f"Позиция: {x[0]}. Название: {x[1]}. Цена: {x[2]}")
    print('\n')


def edit_products():  # Редактирование товаров
    if auth_products():
        do = edit_menu()
        while do != 5:
            connection.commit()
            if do == 1:
                add_product()
            if do == 2:
                edit_product()
            if do == 3:
                delete_product()
            if do == 4:
                menu_products()
            if do not in (1, 2, 3, 4, 5):
                print('Такого пункта нет!')
            do = edit_menu()
    else:
        pass

def edit_menu():  # Меню редактирования товара
    print('\tВыберите вид работы с товаром:\n \
                        1. Добавить товар. \n \
                        2. Редактировать товар.\n \
                        3. Удалить товар \n \
                        4. Посмотреть список товаров. \n \
                        5. Выйти из меню')
    do = int(input('Ваш выбор: '))
    return do


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
    if data == []:
        cost = int(input('Цена товара: '))
        products = (product, cost)
        base_shop.execute(sql, products)
        connection.commit()
    else:
        print('Товар уже существует. Добавить такой же невозможно')
        edit_products()


def edit_product_menu():  # Меню редактирования товара
    print('Изменить цену - 1.\nИзменить название - 2.\nВыход - 3.')
    do = int(input('Ваш выбор: '))
    return do


def edit_product():  # Редактирование товара
    sql = "INSERT INTO products (id,product,cost) values (%s, %s, %s)"
    id_product = input('Введите id товара для редактирования: ')
    base_shop.execute(f"SELECT * from products where id = {id_product}")
    data = base_shop.fetchall()
    if data != []:
        id_product = data[0][0]
        name_product = data[0][1]
        cost_product = data[0][2]
        do = edit_product_menu()
        while do != 3:
            if do == 1:
                print(f'Текущая цена товара "{name_product}" составляет: {cost_product}')
                new_cost = input('Введите новую цену: ')
                base_shop.execute(f"DELETE FROM products WHERE id = {id_product}")
                product = (id_product, name_product, new_cost)
                base_shop.execute(sql,product)
                connection.commit()
                return
            if do == 2:
                print(f'Текущее название товара: "{name_product}"')
                new_name = input('Введите новое название: ')
                base_shop.execute(f"DELETE FROM products WHERE id = {id_product}")
                product = (id_product, new_name, cost_product)
                base_shop.execute(sql, product)
                connection.commit()
                return
            if do not in (1,2,3):
                print('Такой команды нет.')
            do = edit_product_menu()

    else:
        print('Такого товара нет.')
        edit_products()


def delete_product():  # Удалить товар
    id_product = input('Введите id товара: ')
    base_shop.execute(f"SELECT * from products where id = {id_product}")
    data = base_shop.fetchall()
    if data != []:
        base_shop.execute(f"DELETE FROM products WHERE id = {id_product}")
        print('Товар удалён.')
        base_shop.execute(f"ALTER TABLE products AUTO_INCREMENT = {id_product}")
        connection.commit()
    else:
        print('Такого товара нет.')
        edit_products()
