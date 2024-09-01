import sqlite3

conn = sqlite3.connect('book.db')

cursor = conn.cursor()

# Creating the tables
cursor.execute("create table if not exists book (isbn INT PRIMARY KEY,title TEXT NOT NULL,author TEXT NOT NULL,publication_year INTEGER)")
cursor.execute("create table if not exists user (id INT PRIMARY KEY,email TEXT NOT NULL)")
cursor.execute('''create table if not exists borrowed (id INTEGER PRIMARY KEY AUTOINCREMENT,book INT NOT NULL,user INT NOT NULL,FOREIGN KEY (book) REFERENCES book(isbn),FOREIGN KEY (user) REFERENCES user(id))''')

cursor.execute("delete from book")
cursor.execute("delete from user")
cursor.execute("delete from borrowed")

cursor.execute("insert into user values(1,'manavshah1011.ms@gmail.com')")


cursor.execute("select * from book")
print(cursor.fetchall())
cursor.execute("select * from user")
print(cursor.fetchall())
cursor.execute("select * from borrowed")
print(cursor.fetchall())

conn.commit()
conn.close()
