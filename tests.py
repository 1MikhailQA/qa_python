from main import BooksCollector
import unittest

class TestBooksCollector(unittest.TestCase):

    def setUp(self):
        self.collector = BooksCollector()

    def test_add_new_book(self):
        self.collector.add_new_book("Book1")
        self.assertIn("Book1", self.collector.get_books_genre())

    def test_set_book_genre(self):
        self.collector.add_new_book("Book2")
        self.collector.set_book_genre("Book2", "Фантастика")
        self.assertEqual(self.collector.get_book_genre("Book2"), "Фантастика")

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book("Book3")
        self.collector.set_book_genre("Book3", "Фантастика")
        self.assertEqual(self.collector.get_books_with_specific_genre("Фантастика"), ["Book3"])


    def test_add_book_in_favorites(self):
        self.collector.add_new_book("Book4")
        self.collector.add_book_in_favorites("Book4")
        self.assertIn("Book4", self.collector.get_list_of_favorites_books())

    def test_delete_book_from_favorites(self):
        self.collector.add_new_book("Book5")
        self.collector.add_book_in_favorites("Book5")
        self.collector.delete_book_from_favorites("Book5")
        self.assertNotIn("Book5", self.collector.get_list_of_favorites_books())

    def test_add_book_in_favorites_invalid_book(self):
        self.collector.add_book_in_favorites("InvalidBook")
        self.assertNotIn("InvalidBook", self.collector.get_list_of_favorites_books())

    def test_get_book_genre_missing_genre(self):
        self.assertIsNone(self.collector.get_book_genre("NonExistingBook"))

    def test_get_books_with_specific_genre_invalid_genre(self):
        self.assertEqual(self.collector.get_books_with_specific_genre("InvalidGenre"), [])

    def test_get_books_for_children_with_books(self):
        self.collector.add_new_book("Book6")
        self.collector.set_book_genre("Book6", "Комедии")
        self.assertEqual(self.collector.get_books_for_children(), ["Book6"])


if __name__ == "__main__":
    unittest.main()