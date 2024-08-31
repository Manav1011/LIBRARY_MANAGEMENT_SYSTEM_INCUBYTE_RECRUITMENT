import unittest

# here is the test which will satisfy the rule 1 of Test driven development

class TestMultiplyFunction(unittest.TestCase):
    def setUp(self):
        self.LMS = LibraryManagement()
    
    def test_return_book_which_is_not_borrowed(self):
        # I'm simply raising an assertion error  when the returned book is not even borrowed
        with self.assertRaises(Exception) as context:
            self.LMS.read_book('dummy-isbn')
        self.assertEqual(str(context.exception),'book_not_borrowed')
        

if __name__ == '__main__':
    unittest.main()