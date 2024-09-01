import unittest

# Discover and run all tests in the "tests" folder
loader = unittest.TestLoader()
suite = loader.discover('tests')
print(suite)


runner = unittest.TextTestRunner()
runner.run(suite)