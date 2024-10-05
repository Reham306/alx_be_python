class Book:
    """Class to represent a book in the library."""
    
    def __init__(self, title, author):
        """Initialize the book with a title and author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to the library."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Class to represent a library that manages books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'.")
                    return
                else:
                    print(f"'{title}' is not currently checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")


