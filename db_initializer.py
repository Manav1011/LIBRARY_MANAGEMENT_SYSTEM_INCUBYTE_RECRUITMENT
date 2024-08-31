import sqlite3

conn = sqlite3.connect('book.db')

cursor = conn.cursor()

cursor.execute("create table if not exists book (isbn TEXT PRIMARY KEY,title TEXT NOT NULL,author TEXT NOT NULL,publication_year INTEGER)")

conn.commit()
conn.close()
