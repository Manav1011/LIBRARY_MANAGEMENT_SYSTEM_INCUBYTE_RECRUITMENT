import sqlite3

conn = sqlite3.connect('book.db')

cursor = conn.cursor()

# Creating the tables
cursor.execute("create table if not exists book (isbn INT PRIMARY KEY,title TEXT NOT NULL,author TEXT NOT NULL,publication_year INTEGER)")
cursor.execute("create table if not exists user (id INT PRIMARY KEY,email TEXT NOT NULL)")
cursor.execute('''create table if not exists borrowed (id INT PRIMARY KEY,book INT NOT NULL,user INT NOT NULL,FOREIGN KEY (book) REFERENCES book(isbn),FOREIGN KEY (user) REFERENCES user(id))''')

cursor.execute("select * from book")
print(cursor.fetchall())
conn.commit()
conn.close()
