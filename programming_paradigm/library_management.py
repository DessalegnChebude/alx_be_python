class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._book = []   # Private list to store books.

    def add_book(self, book):
        self._book.append(book)  #adding book to library.
    

    def check_out_book(self, title):
        for book in self._book:
            if book.title == title:
                if book.check_out():
                    print(f"Book '{title}' has been checked out.")
                    return True
                else:
                    print(f"Book '{title}' is already checked out.")
                    return False
        print(f'Book "{title}" not found in the library.')
        return False

    def return_book(self, title):
        for book in self._book:
            if book.title == title:
                if book.return_book():
                    print(f"Book '{title}' has been returned.")
                    return True
            else:
                print(f"Book '{title}' was not checked out")
                return False
        print(f'Book "{title}" not found in the library.')
        return False
    
    def list_available_books(self):
        avalable_books = [book.title for book in self._book if book.is_available()]
        if avalable_books:
            print("Available books:")
            for title in avalable_books:
                print(f"- {title}")
        else:
            print("No books are currently available.")
