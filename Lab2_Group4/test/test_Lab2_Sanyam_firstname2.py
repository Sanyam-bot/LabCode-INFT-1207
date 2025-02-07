import unittest
from src.Lab2_Sanyam_firstname2 import add_book, list_books, search_book


class TestReadingList(unittest.TestCase):
    def test_add_book(self):
        add_book("Test Book", "Author Name", 2022)
        # Assert if the book is added (by manually checking CSV or creating validation logic)

    def test_search_book(self):
        search_book("Test Book")
        # Assert the output of the search

    # More test cases to be added...


if __name__ == '__main__':
    unittest.main()