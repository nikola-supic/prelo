"""
DOCSTRING:

"""

# Importing the libraries
from datetime import datetime, date
import mysql.connector

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

# songs-related functions
def add_song(artist, name, path, length, added_by):
    sql = "SELECT * FROM artist WHERE name=%s"
    val = (artist, )
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result is None:
        sql = "INSERT INTO artist (name) VALUES (%s)"
        val = (artist, )
        mycursor.execute(sql, val)
        mydb.commit()
        artist_id = mycursor.lastrowid
    else:
        artist_id = result[0]

    sql = "INSERT INTO song (artist_id, name, path, length, added_by) VALUES (%s, %s, %s, %s, %s)"
    val = (artist_id, name, path, length, added_by, )
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid

# user-related functions
def get_party_user(user_id):
    sql = "SELECT username FROM user WHERE id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result