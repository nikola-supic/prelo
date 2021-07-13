"""
DOCSTRING:

"""

from datetime import datetime, timedelta, date
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='prelo'
        )
    mycursor = mydb.cursor(buffered=True)
    print('[ + ] Successfully connected to database.')
except mysql.connector.errors.InterfaceError: 
    print('[ - ] Can not connect to database.')


# user-related functions
class User():
    """
    DOCSTRING:

    """
    def __init__(self, result):
        self.id = result[0]
        self.first_name = result[1]
        self.last_name = result[2]
        self.username = result[3]
        self.email = result[4]
        self.password = result[5]
        self.birthday = result[6]
        self.admin = result[7]
        self.register_date = result[8]
        self.online = True # 9
        self.last_online = datetime.now() # 10

        sql = "UPDATE user SET last_online=%s, online=1 WHERE id=%s"
        val = (self.last_online, self.id, )
        mycursor.execute(sql, val)
        mydb.commit()


    def user_quit(self):
        self.last_online = datetime.now()
        self.online = False

        sql = "UPDATE user SET last_online=%s, online=0 WHERE id=%s"
        val = (self.last_online, self.id, )

        mycursor.execute(sql, val)
        mydb.commit()


    def update_sql(self, column, value):
        sql = f"UPDATE user SET {column}=%s WHERE id=%s"
        val = (value, self.id, )
        mycursor.execute(sql, val)
        mydb.commit()


def check_login(username, password):
    sql = "SELECT * FROM user WHERE username=%s AND password=%s"
    val = (username, password, )

    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result is not None:
        return User(result)
    return None


def check_register(first_name, last_name, username, email, password, confirm_pw):
    if len(first_name) < 4:
        return False
    if len(last_name) < 4:
        return False
    if len(username) < 4:
        return False
    if len(email) < 4:
        return False
    if len(password) < 8 or len(password) > 24:
        return False
    if password != confirm_pw:
        return False

    try:
        sql = "INSERT INTO user (first_name, last_name, username, email, password, birthday, register_date) VALUES (%s, %s, %s, %s, %s, %s, NOW())"
        val = (first_name, last_name, username, email, password, date(1970, 1, 1), )

        mycursor.execute(sql, val)
        mydb.commit()

        return True
    except Exception as e:
        print(e)
    return False


def search_user(username):
    sql = "SELECT id, username FROM user WHERE username LIKE %s"
    val = (username, )

    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result


def change_name(user_id, first_name, last_name):
    sql = "UPDATE user SET first_name = %s, last_name = %s WHERE id = %s"
    val = (first_name, last_name, user_id, )

    mycursor.execute(sql, val)
    mydb.commit()


def delete_user(user_id):
    sql = "DELETE FROM user WHERE id = %s"
    val = (user_id, )

    mycursor.execute(sql, val)
    mydb.commit()


def get_online():
    mycursor.execute("SELECT id, first_name, last_name FROM user WHERE online=1")
    result = mycursor.fetchall()
    return result


def get_name(user_id):
    sql = "SELECT first_name, last_name FROM user WHERE id = %s"
    val = (user_id, )

    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return f'{result[0]} {result[1]}'


def get_username(user_id):
    sql = "SELECT username FROM user WHERE id = %s"
    val = (user_id, )

    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result[0]