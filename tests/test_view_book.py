import unittest
from LMS.library_management import LibraryManagement

# here is the test which will satisfy the rule 1 of Test driven development

class TestMultiplyFunction(unittest.TestCase):
    def setUp(self):
        self.LMS = LibraryManagement()
    
    def test_view_books_returns_list(self):
        # I'm simply requesting all the books and making sure the functions returns an array
        self.books = self.LMS.get_books()    
        self.assertIsInstance(self.books,list,"The return type of get_books_should be a list only!!")
        

if __name__ == '__main__':
    unittest.main()