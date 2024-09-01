import unittest
from library_management import LibraryManagement

# here is the test which will satisfy the rule 1 of Test driven development

class TestMultiplyFunction(unittest.TestCase):
    def setUp(self):
        self.LMS = LibraryManagement()
    
    def test_return_book_using_wrong_ISBN(self):
        # I'm simply raising an assertion error  when ISBN is a stirng type
        with self.assertRaises(Exception) as context:
            self.LMS.return_book('dummy-isbn','dummy-user-id')
        self.assertEqual(str(context.exception),'book_not_found')
        

if __name__ == '__main__':
    unittest.main()