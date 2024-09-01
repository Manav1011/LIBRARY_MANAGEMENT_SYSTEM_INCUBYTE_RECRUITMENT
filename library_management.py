import sqlite3
from datetime import datetime
import re

class LibraryManagement():
    def __init__(self):
        self.conn = sqlite3.connect('book.db')
        self.cursor = self.conn.cursor()

    def add_book(self,isbn,title,author,publication_year):
        
        # for the test case test_check_for_null_values
        if isbn is None or title is None or author is None or publication_year is None:
            raise Exception('parameters_missing')        
        
        # for the test_add_book_string_ISBN
        if not isinstance(isbn, int):
            raise Exception('type_mismatch_for_isbn')

        # For the test_add_book_string_title
        if not isinstance(title, str):
            raise Exception('type_mismatch_for_title')

        # For the test_add_book_string_author
        if not isinstance(author, str):
            raise Exception('type_mismatch_for_author')

        # For the test_add_book_int_publication_year
        if not isinstance(publication_year, int):
            raise Exception('type_mismatch_for_publication_year')

        # for the test_future_publication_year
        current_year = datetime.now().year
        if publication_year > current_year:
            raise Exception('wrong_publication_year')

        # For the test_minimum_title_length
        if len(title) < 2:
            raise Exception('title_length_too_low')

        # For the test_special_characters_in_title
        if re.search(r'[^a-zA-Z0-9\s]', title):
            raise Exception('special_characters_are_not_allowed')
    
        return True

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
