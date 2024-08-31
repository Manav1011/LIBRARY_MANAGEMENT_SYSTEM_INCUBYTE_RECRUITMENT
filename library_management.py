import sqlite3

class LibraryManagement():
    def __init__(self):
        self.conn = sqlite3.connect('book.db')
        self.cursor = self.conn.cursor()

    def add_book(self,isbn):
        pass