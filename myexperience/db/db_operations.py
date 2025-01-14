
import sqlite3

def inserttodb(query):
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

def update(query):
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

def delete(query):
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

def select(query):
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
