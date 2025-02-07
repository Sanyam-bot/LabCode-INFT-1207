import io
import os
import csv
import unittest
from unittest.mock import patch
from src.Lab2_Sanyam_Anchal import add_book, list_books, search_book, delete_book

# Change working directory to the project root
os.chdir(os.path.dirname(os.path.dirname(__file__)))


class TestReadingList(unittest.TestCase):
    def test_add_book(self):
        add_book("Test Book", "Test Book", 2022)
        with open('src/books.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row == ['Test Book', 'Test Book', '2022']:
                    result = True
                    break
                else:
                    result = False
        self.assertTrue(result)

    def test_add_book_empty_inputs(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mocked_stdout:
            result = add_book('', '', '')  # Call function with empty inputs

            # Get captured output
            output = mocked_stdout.getvalue().strip()

            # Check if the printed message matches the expected error
            self.assertIn("Error: The input cannot be empty for title, author, and year.", output)
            self.assertEqual(result, 1)

    def test_add_book_string_year(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mocked_stdout:
            result = add_book('title', 'author', '2005f')

            # Get captured output
            output = mocked_stdout.getvalue().strip()

            # Check if the printed message matches the expected error
            self.assertIn("Error: The year input needs to be an integer.", output)
            self.assertEqual(result, 1)

    def test_add_book_lower_bound_year(self):
        add_book('Ruthenium', 'yulu', '1500')
        with open('src/books.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row == ['Ruthenium', 'yulu', '1500']:
                    result = True
                    break
                else:
                    result = False
        self.assertTrue(result)

    def test_add_book_upper_bound_year(self):
        add_book('Ruthenium', 'yulu', '2025')
        with open('src/books.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            result = False
            for row in reader:
                if row == ['Ruthenium', 'yulu', '2025']:
                    result = True
                    break
        self.assertTrue(result)

    def test_add_book_middle_year(self):
        add_book('Ruthenium', 'yulu', '1750')
        with open('src/books.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            result = False
            for row in reader:
                if row == ['Ruthenium', 'yulu', '1750']:
                    result = True
                    break
        self.assertTrue(result)

    def test_search_book_found(self):
        result = search_book('1984')
        self.assertEqual(result, 0)

    def test_search_book_not_found(self):
        result = search_book('1985')
        self.assertEqual(result, 1)

    def test_delete_book_found(self): # Checked manually in the books.csv
        result = delete_book('Moby')
        self.assertEqual(result, 0)

    def test_delete_book_not_found(self): # Checked manually in the books.csv
        result = delete_book('Mobi')
        self.assertEqual(result, 1)

    def test_list_books(self): # Checked manually on the console
        result = list_books()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()