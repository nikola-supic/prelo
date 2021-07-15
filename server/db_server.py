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
    sql = "INSERT INTO song (artist, name, path, length, added_by) VALUES (%s, %s, %s, %s, %s)"
    val = (artist, name, path, length, added_by, )

    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid