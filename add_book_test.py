import unittest

# here is the test which will satisfy the rule 1 of Test driven development

class TestMultiplyFunction(unittest.TestCase):
    def setUp(self):
        self.LMS = LibraryManagement()
    
    def test_add_book_string_ISBN(self):
        # I'm simply raising an assertion error  when ISBN is a stirng type
        with self.assertRaises(TypeError):
            self.LMS.add_book('dummy-isbn','Test Book','Test Author',2024)
        

if __name__ == '__main__':
    unittest.main()