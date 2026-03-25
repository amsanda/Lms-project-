# Class to represent a library member
class Member:
    """Represents a library member."""  # Docstring describing the class

    MAX_BORROW_LIMIT = 5  # Maximum books a member can borrow

    # Constructor to initialize member data
    def __init__(self, name, member_id, email):
        self._name = name               # Private variable for member name
        self._member_id = member_id     # Private variable for member ID
        self._email = email             # Private variable for email
        self._borrowed_books = []       # List to store borrowed books
        self._fines_owed = 0.0          # Fines the member owes

    # Property to safely access the member's name
    @property
    def name(self):
        return self._name

    # Property to safely access the member's ID
    @property
    def member_id(self):
        return self._member_id

    # Method to borrow a book if under the borrow limit
    def borrow_book(self, book):
        """Borrow a book if within limits."""
        if len(self._borrowed_books) >= Member.MAX_BORROW_LIMIT:
            return False  # Cannot borrow more than limit
        self._borrowed_books.append(book)
        return True

    # Method to return a borrowed book
    def return_book(self, book):
        """Return a borrowed book."""
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            return True
        return False

    # Method to get a copy of borrowed books (to protect internal data)
    def get_borrowed_books(self):
        """Return a copy of the borrowed books list."""
        return self._borrowed_books.copy()

    # Method to add fines
    def add_fine(self, amount):
        """Add a fine to the member's account."""
        self._fines_owed += amount

    # Method to pay fines
    def pay_fine(self, amount):
        """Pay part or all of fines owed."""
        if amount > self._fines_owed:
            amount = self._fines_owed
        self._fines_owed -= amount
        return amount

    # Method to check fines owed
    def get_fines_owed(self):
        return self._fines_owed