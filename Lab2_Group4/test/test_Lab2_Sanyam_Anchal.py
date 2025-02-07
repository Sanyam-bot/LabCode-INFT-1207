import os
import csv
import unittest
from Lab2_Sanyam_Anchal import add_book  # Ensure this import works

# Change working directory to the project root
os.chdir(os.path.dirname(os.path.dirname(__file__)))

# class TestReadingList(unittest.TestCase):
#     def test_add_book(self):
#         add_book("Test Book", "Test Book", 2022)
#
#         # Now we can use a simple relative path
#         with open('src/books.csv', mode='r', newline='') as file:
#             reader = csv.reader(file)
#             result = any(row == ['Test Book', 'Test Book', '2022'] for row in reader)
#
#         self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
