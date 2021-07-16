"""
DOCSTRING:

"""

from datetime import datetime, date
import mysql.connector
from utils import empty_temp

# Global variables
global mydb, mycursor
def connect(host='localhost', user='root', password='', database=''):
    try:
        global mydb, mycursor
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=database
            )
        mycursor = mydb.cursor(buffered=True)
        print('[ + ] Successfully connected to database.')
        return True
    except mysql.connector.errors.InterfaceError: 
        print('[ - ] Can not connect to database.')
        return False

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

        empty_temp()


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
    if len(email) < 8:
        return False
    if len(password) < 8 or len(password) > 48:
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
    sql = "SELECT id, first_name, last_name, username FROM user WHERE username LIKE CONCAT('%',%s,'%')"
    val = (username, )

    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


def get_name(user_id):
    sql = "SELECT first_name, last_name FROM user WHERE id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return f'{result[0]} {result[1]}'


def get_username(user_id):
    sql = "SELECT username FROM user WHERE id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result[0]


# friends related functions
def add_friend(user_id, friend_id):
    sql = "SELECT id FROM friends WHERE (user_id=%s AND friend_id=%s) OR (friend_id=%s AND user_id=%s)"
    val = (user_id, friend_id, user_id, friend_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result is None:
        sql = "INSERT INTO friends (user_id, friend_id, request) VALUES (%s, %s, %s)"
        val = (user_id, friend_id, True)
        mycursor.execute(sql, val)
        mydb.commit()
        return True
    return False


def get_sent_requests(user_id):
    sql = "SELECT id, friend_id FROM friends WHERE user_id=%s AND request=1"
    val = (user_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


def get_requests(friend_id):
    sql = "SELECT id, user_id FROM friends WHERE friend_id=%s AND request=1"
    val = (friend_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


def get_friends(user_id):
    sql = "SELECT friend_id, user_id, id FROM friends WHERE (friend_id=%s OR user_id=%s) AND request=0"
    val = (user_id, user_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


def delete_request(request_id):
    sql = "DELETE FROM friends WHERE id=%s"
    val = (request_id, )
    mycursor.execute(sql, val)
    mydb.commit()


def accept_request(request_id):
    sql = "UPDATE friends SET request=0 WHERE id=%s"
    val = (request_id, )
    mycursor.execute(sql, val)
    mydb.commit()


def delete_friend(user_id, friend_id):
    sql = "DELETE FROM friends WHERE (user_id=%s AND friend_id=%s) OR (friend_id=%s AND user_id=%s)"
    val = (user_id, friend_id, user_id, friend_id, )
    mycursor.execute(sql, val)
    mydb.commit()


# chat-related functions
def send_message(user_id, friend_id, message):
    sql = "INSERT INTO chat (user_id, friend_id, message) VALUES (%s, %s, %s)"
    val = (user_id, friend_id, message, )
    mycursor.execute(sql, val)
    mydb.commit()


def get_chat(user_id, friend_id):
    mydb.commit()

    sql = "SELECT * FROM chat WHERE (user_id=%s AND friend_id=%s) OR (friend_id=%s AND user_id=%s)"
    val = (user_id, friend_id, user_id, friend_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


# artist-related functions
def get_artist_name(artist_id):
    sql = "SELECT name FROM artist WHERE id=%s"
    val = (artist_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result[0]


def get_artist_count(artist_id):
    sql = "SELECT COUNT(id) AS count FROM song WHERE artist_id=%s"
    val = (artist_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result[0]

def get_artist_songs(artist_id):
    sql = "SELECT id FROM song WHERE artist_id=%s"
    val = (artist_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result



# songs-releated functions
class Song():
    def __init__(self, song_id):
        super(Song, self).__init__()
        self.song_id = song_id

        sql = "SELECT * FROM song WHERE id=%s"
        val = (song_id, )
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        self.artist_id = result[1]
        self.name = result[2]
        self.art = result[3]
        self.path = result[4]
        self.length = result[5]
        self.added_by = result[6]


def search_song(name):
    sql = "SELECT id, artist_id, name FROM song WHERE name LIKE CONCAT('%',%s,'%')"
    val = (name, )

    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


# user-songs
def add_user_song(user_id, song_id):
    sql = "SELECT id FROM user_song WHERE user_id=%s AND song_id=%s"
    val = (user_id, song_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result is None:
        sql = "INSERT INTO user_song (user_id, song_id) VALUES (%s, %s)"
        val = (user_id, song_id, )
        mycursor.execute(sql, val)
        mydb.commit()
        return True
    return False


def get_user_songs(user_id):
    sql = "SELECT song_id FROM user_song WHERE user_id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


def get_user_artist(user_id):
    sql = "SELECT DISTINCT artist_id FROM song WHERE id IN (SELECT song_id FROM user_song WHERE user_id=%s)"
    val = (user_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


# user-recent functions
def add_user_recent(user_id, song_id):
    sql = "SELECT COUNT(id) AS count FROM user_recent WHERE user_id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    count = mycursor.fetchone()[0]

    if count >= 20:
        sql = "DELETE FROM user_recent WHERE user_id=%s LIMIT 1"
        val = (user_id, )
        mycursor.execute(sql, val)
        mydb.commit()

    sql = "INSERT INTO user_recent (user_id, song_id) VALUES (%s, %s)"
    val = (user_id, song_id, )
    mycursor.execute(sql, val)
    mydb.commit()


def get_user_recent(user_id):
    sql = "SELECT song_id FROM user_recent WHERE user_id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


# playlist functions
def create_playlist(user_id, name, description, public):
    sql = "INSERT INTO playlist (creator_id, name, description, public) VALUES (%s, %s, %s, %s)"
    val = (user_id, name, description, public, )
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid


def get_playlist_name(playlist_id):
    sql = "SELECT name FROM playlist WHERE id=%s"
    val = (playlist_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result[0]


def add_playlist_song(playlist_id, song_id):
    sql = "INSERT INTO playlist_song (playlist_id, song_id) VALUES (%s, %s)"
    val = (playlist_id, song_id, )
    mycursor.execute(sql, val)
    mydb.commit()


def get_playlist_songs(playlist_id):
    sql = "SELECT song_id FROM playlist_song WHERE playlist_id=%s"
    val = (playlist_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


# user-playlist functions
def get_user_playlist(user_id):
    sql = "SELECT playlist_id FROM user_playlist WHERE user_id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


def add_user_playlist(user_id, playlist_id):
    sql = "INSERT INTO user_playlist (user_id, playlist_id) VALUES (%s, %s)"
    val = (user_id, playlist_id, )
    mycursor.execute(sql, val)
    mydb.commit()