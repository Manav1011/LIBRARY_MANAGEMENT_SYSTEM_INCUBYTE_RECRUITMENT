import sqlite3
from datetime import datetime
import re

class LibraryManagement():
    def __init__(self) -> None:
        self.conn = sqlite3.connect('book.db')        
        self.cursor = self.conn.cursor()

    def get_user(self,email) -> list:
        self.cursor.execute('select * from user where email=?',(email,))
        self.user = self.cursor.fetchall()
        if len(self.user) > 0:
            return self.user
        else:return None
        
    def add_book(self, isbn: int, title: str, author: str, publication_year: int) -> bool:
        
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
        
        try:
            self.cursor.execute('insert into book VALUES (?, ?, ?, ?)', (isbn, title, author, publication_year))
        except sqlite3.IntegrityError as e:            
            raise Exception('book_already_exists')
        finally:
            self.conn.commit()            
    
        return True

    def borrow_book(self, isbn: int, user_id: int) -> bool:

        # for the test case test_check_for_null_values
        if isbn is None or user_id is None:            
            raise Exception('parameters_missing')        

        # for the test_borrow_book_non_int_ISBN
        if not isinstance(isbn, int):
            raise Exception('type_mismatch_for_isbn')
        
        # for the test_borrow_book_non_int_user_id
        if not isinstance(user_id, int):
            raise Exception('type_mismatch_for_user_id')        

        # for the test_borrow_book_using_wrong_ISBN
        self.cursor.execute('SELECT isbn FROM book WHERE isbn = ?', (isbn,))
        self.book = self.cursor.fetchall()        
        if len(self.book) == 0:
            raise Exception('book_not_found')
        
        # For the test_borrower_exists
        self.cursor.execute('SELECT id FROM user WHERE id = ?', (user_id,))
        self.user = self.cursor.fetchall()
        if len(self.user) == 0:
            raise Exception('borrower_does_not_exists')
        
        # For the test_book_already_borrowed
        self.cursor.execute('''
        SELECT b.isbn
        FROM book b
        JOIN borrowed br ON br.book = b.isbn
        JOIN user u ON br.user = u.id
        WHERE u.id = ? AND b.isbn = ?
        ''',(user_id, isbn))
        
        if len(self.cursor.fetchall()) > 0:
            raise Exception('book_already_borrowed')
        
        try:                        
            self.cursor.execute('INSERT INTO borrowed (book, user) VALUES (?, ?)', (isbn, user_id))
        except sqlite3.IntegrityError as e:
            print(e)
        finally:
            self.conn.commit()            

        return True
    
    def return_book(self, isbn: int, user_id: int) -> bool:
        
        # For test_check_for_null_values
        if isbn is None or user_id is None:
            raise Exception('parameters_missing')        

        # For the test_return_book_string_ISBN
        if not isinstance(isbn, int):
            raise Exception('type_mismatch_for_isbn')
        
        # For the test_return_book_string_user_id
        if not isinstance(user_id, int):
            raise Exception('type_mismatch_for_user_id')

        # For the test_return_book_using_wrong_ISBN
        self.cursor.execute('SELECT isbn FROM book WHERE isbn = ?', (isbn,))        
        self.book = self.cursor.fetchall()        
        if len(self.book) == 0:
            raise Exception('book_not_found')
        
        # For the test_returner_exists
        self.cursor.execute('SELECT id FROM user WHERE id = ?', (user_id,))
        self.user = self.cursor.fetchall()
        if len(self.user) == 0:
            raise Exception('returner_does_not_exists')

        # for the test_book_is_not_borrowed
        self.cursor.execute('''
        SELECT b.isbn
        FROM book b
        JOIN borrowed br ON br.book = b.isbn
        JOIN user u ON br.user = u.id
        WHERE u.id = ? AND b.isbn = ?
        ''', (user_id, isbn))

        if len(self.cursor.fetchall()) == 0:
            raise Exception('book_is_not_borrowed')

        try:                        
            self.cursor.execute('Delete from borrowed where book=?', (isbn,))
        except sqlite3.IntegrityError as e:
            print(e)
        finally:
            self.conn.commit()            
        
        return True

    # For the test_view_books_returns_list
    def get_books(self) -> list:
        self.cursor.execute(f'select * from book')
        self.books = self.cursor.fetchall()        
        return self.books
