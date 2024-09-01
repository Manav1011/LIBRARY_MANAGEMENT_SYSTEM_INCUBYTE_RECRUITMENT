import unittest
from library_management import LibraryManagement
from datetime import datetime


# here is the test which will satisfy the rule 1 of Test driven development

class TestMultiplyFunction(unittest.TestCase):
    def setUp(self):
        self.LMS = LibraryManagement()    
    
    def test_check_for_null_values(self):
        # I'm simply raising an assertion error when any of the input parameter is null or not defined
        self.assertRaises(Exception, self.LMS.add_book,None,'Test Book','Test Author',2024)
        self.assertRaises(Exception, self.LMS.add_book,1,None,'Test Author',2024)
        self.assertRaises(Exception, self.LMS.add_book,1,"Test Book",None,2024)
        self.assertRaises(Exception, self.LMS.add_book,1,'Test Book','Test Author',None)
        self.assertRaises(Exception, self.LMS.add_book,None,None,None,None)
        self.assertRaises(Exception, self.LMS.add_book)

    def test_add_book_non_int_ISBN(self):
        # I'm simply raising an assertion error  when ISBN is a stirng type
        with self.assertRaises(Exception) as e:
            self.LMS.add_book("1",'Test Book','Test Author',2024)
        self.assertEqual(str(e.exception),'type_mismatch_for_isbn')

    def test_add_book_string_title(self):
        # I'm simply raising an assertion error  when title is a stirng type
        with self.assertRaises(Exception) as e:
            self.LMS.add_book(1,bool,'Test Author',2024)
        self.assertEqual(str(e.exception),'type_mismatch_for_title')
    
    def test_add_book_string_author(self):
        # I'm simply raising an assertion error  when author is a stirng type
        with self.assertRaises(Exception) as e:
            self.LMS.add_book(1,'Test Book',dict,2024)
        self.assertEqual(str(e.exception),'type_mismatch_for_author')

    def test_add_book_non_int_publication_year(self):
        # I'm simply raising an assertion error  when publication_year is a int type
        with self.assertRaises(Exception) as e:
            self.LMS.add_book(1,'Test Book','Test Author',"2024")
        self.assertEqual(str(e.exception),'type_mismatch_for_publication_year')
    
    def test_future_publication_year(self):
        # I'm simply raising an assertion error  when publication_year is either current year or a future year        
        with self.assertRaises(Exception) as e:
            self.LMS.add_book(1,'Test Book','Test Author',2026)
        self.assertEqual(str(e.exception),'wrong_publication_year')

    def test_minimum_title_length(self):
        # I'm simply raising an assertion error  when title_length is less then 2 characters
        with self.assertRaises(Exception) as e:
            self.LMS.add_book(1,'T','Test Author',2024)
        self.assertEqual(str(e.exception),'title_length_too_low')
    
    def test_special_characters_in_title(self):
        # I'm simply raising an assertion error  when there are any special characters in the title
        with self.assertRaises(Exception) as e:
            self.LMS.add_book(1,'Test $ Book','Test Author',2024)
        self.assertEqual(str(e.exception),'special_characters_are_not_allowed')

    def test_book_duplication(self):
        # I'm simply raising an assertion error  when someone tries to add a book with same isbn twice
        try:
            with self.assertRaises(Exception) as e:
                self.result = self.LMS.add_book(1,'Test Book','Test Author',2024)
                self.assertEqual(str(e.exception),'book_already_exists')
        except Exception as e:
            self.assertIsInstance(self.result,bool,"The return type of add_book should be a boolean only!!")            


if __name__ == '__main__':
    unittest.main()