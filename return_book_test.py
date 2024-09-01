import unittest
from library_management import LibraryManagement

# here is the test which will satisfy the rule 1 of Test driven development

class TestMultiplyFunction(unittest.TestCase):
    def setUp(self):
        self.LMS = LibraryManagement()
    
    def test_check_for_null_values(self):
        # I'm simply raising an assertion error when any of the input parameter is null or not defined
        self.assertRaises(Exception, self.LMS.return_book,None,1)
        self.assertRaises(Exception, self.LMS.return_book,1,None)        
        self.assertRaises(Exception, self.LMS.return_book,None,None)
        self.assertRaises(Exception, self.LMS.return_book)
    
    def test_return_book_non_int_ISBN(self):
        # I'm simply raising an assertion error  when ISBN is a stirng type
        with self.assertRaises(Exception) as e:
            self.LMS.return_book("1",1)
        self.assertEqual(str(e.exception),'type_mismatch_for_isbn')
    
    def test_return_book_non_int_user_id(self):
        # I'm simply raising an assertion error  when user_id is a stirng type
        with self.assertRaises(Exception) as e:
            self.LMS.return_book(1,"1")
        self.assertEqual(str(e.exception),'type_mismatch_for_user_id')
        
    def test_return_type_is_boolean(self):        
        self.result = self.LMS.return_book(1,1)
        self.assertIsInstance(self.result,bool,"The return type of add_book should be a boolean only!!")        

    def test_return_book_using_wrong_ISBN(self):
        # I'm simply raising an assertion error  when ISBN is a stirng type
        with self.assertRaises(Exception) as context:
            self.LMS.return_book(10,1)
        self.assertEqual(str(context.exception),'book_not_found')
    
    def test_returner_exists(self):
        with self.assertRaises(Exception) as context:
            self.LMS.return_book(1,10)
        self.assertEqual(str(context.exception),'returner_does_not_exists')

    def test_book_is_not_borrowed(self):
        with self.assertRaises(Exception) as context:
            self.LMS.return_book(2,1)
        self.assertEqual(str(context.exception),'book_is_not_borrowed')
        

if __name__ == '__main__':
    unittest.main()