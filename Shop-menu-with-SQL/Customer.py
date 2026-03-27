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


