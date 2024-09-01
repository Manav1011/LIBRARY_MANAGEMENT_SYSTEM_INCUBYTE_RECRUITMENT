import sqlite3

class LibraryManagement():
    def __init__(self):
        self.conn = sqlite3.connect('book.db')
        self.cursor = self.conn.cursor()

    def add_book(self,isbn,title,author,publication_year):
        pass

    def borrow_book(self,isbn):
        self.cursor.execute(f'select isbn from book where isbn="{isbn}"')
        self.book = self.cursor.fetchall()
        if len(self.book) == 0:
            raise Exception('book_not_found')
    
    def return_book(self,isbn):
        self.cursor.execute(f'select isbn from book where isbn="{isbn}"')
        self.book = self.cursor.fetchall()
        if len(self.book) == 0:
            raise Exception('book_not_found')

    def get_books(self):
        self.cursor.execute(f'select * from book')
        self.books = self.cursor.fetchall()        
        return self.books
