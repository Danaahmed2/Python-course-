from abc import ABC, abstractmethod


class Book:
    def __init__(self, book_id, title, author, category, available_copies):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__category = category
        self.__available_copies = available_copies
        self.__borrowed_by = []

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def category(self):
        return self.__category

    @property
    def available_copies(self):
        return self.__available_copies

    @property
    def borrowed_by(self):
        return self.__borrowed_by

    def display_info(self):
        print(f"\nBook ID: {self.__book_id}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Category: {self.__category}")
        print(f"Available Copies: {self.__available_copies}")

    def borrow_book(self, user):
        if self.__available_copies <= 0:
            raise Exception("This book is currently unavailable.")

        if user in self.__borrowed_by:
            raise Exception("You already borrowed this book.")

        self.__available_copies -= 1
        self.__borrowed_by.append(user)

    def return_book(self, user):
        if user not in self.__borrowed_by:
            raise Exception("You did not borrow this book.")

        self.__borrowed_by.remove(user)
        self.__available_copies += 1


class User(ABC):
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__borrowed_books = []

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow(self, book):
        if len(self.__borrowed_books) >= self.max_books:
            raise Exception(
                f"You cannot borrow more than {self.max_books} books."
            )

        book.borrow_book(self)
        self.__borrowed_books.append(book)
        print(f"Book '{book.title}' borrowed successfully.")

    def return_book(self, book):
        if book not in self.__borrowed_books:
            raise Exception("You did not borrow this book.")

        book.return_book(self)
        self.__borrowed_books.remove(book)
        print(f"Book '{book.title}' returned successfully.")

    @abstractmethod
    def show_menu(self):
        pass


class Student(User):
    max_books = 3

    def show_menu(self):
        print("\n===== Student Menu =====")
        print("1. Display all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display available books")
        print("5. Display borrowed books")
        print("6. Exit")


class Teacher(User):
    max_books = 5

    def show_menu(self):
        print("\n===== Teacher Menu =====")
        print("1. Display all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display available books")
        print("5. Display borrowed books")
        print("6. Exit")


class Librarian(User):
    max_books = 0

    def show_menu(self):
        print("\n===== Librarian Menu =====")
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Display available books")
        print("8. Display borrowed books")
        print("9. Exit")

    def add_book(self, library, book):
        for existing_book in library:
            if existing_book.book_id == book.book_id:
                raise Exception("A book with this ID already exists.")

        library.append(book)
        print("Book added successfully.")

    def remove_book(self, library, book_id):
        for book in library:
            if book.book_id == book_id:
                if len(book.borrowed_by) > 0:
                    raise Exception("Cannot remove a borrowed book.")

                library.remove(book)
                print("Book removed successfully.")
                return

        raise Exception("Book not found.")

    def search_books(self, library, keyword):
        found = []

        for book in library:
            if (
                keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
                or keyword.lower() in book.category.lower()
            ):
                found.append(book)

        if not found:
            print("No books found.")
            return

        print("\n===== Search Results =====")
        for book in found:
            book.display_info()


def get_integer(message):
    while True:
        try:
            value = int(input(message))

            if value < 0:
                raise ValueError

            return value

        except ValueError:
            print("Invalid numeric input. Please enter a valid number.")


def display_all_books(library):
    if not library:
        print("\nNo books available in the library.")
        return

    print("\n===== All Books =====")

    for book in library:
        book.display_info()


def display_available_books(library):
    available = [book for book in library if book.available_copies > 0]

    if not available:
        print("\nNo available books.")
        return

    print("\n===== Available Books =====")

    for book in available:
        book.display_info()


def display_borrowed_books(library):
    borrowed = [book for book in library if len(book.borrowed_by) > 0]

    if not borrowed:
        print("\nNo books are currently borrowed.")
        return

    print("\n===== Borrowed Books =====")

    for book in borrowed:
        print(f"\nBook ID: {book.book_id}")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Borrowed by: {', '.join(user.name for user in book.borrowed_by)}")


def find_book(library, book_id):
    for book in library:
        if book.book_id == book_id:
            return book

    raise Exception("Book not found.")


def add_book_process(librarian, library):
    try:
        book_id = get_integer("Enter Book ID: ")

        title = input("Enter Title: ").strip()
        author = input("Enter Author: ").strip()
        category = input("Enter Category: ").strip()

        available_copies = get_integer("Enter Available Copies: ")

        if not title or not author or not category:
            raise Exception("Book information cannot be empty.")

        book = Book(
            book_id,
            title,
            author,
            category,
            available_copies
        )

        librarian.add_book(library, book)

    except Exception as e:
        print(f"Error: {e}")


def remove_book_process(librarian, library):
    try:
        book_id = get_integer("Enter Book ID to remove: ")
        librarian.remove_book(library, book_id)

    except Exception as e:
        print(f"Error: {e}")


def search_book_process(librarian, library):
    keyword = input("Enter title, author, or category: ").strip()

    if not keyword:
        print("Search cannot be empty.")
        return

    librarian.search_books(library, keyword)


def borrow_book_process(user, library):
    try:
        if isinstance(user, Librarian):
            print("Librarians cannot borrow books in this system.")
            return

        book_id = get_integer("Enter Book ID to borrow: ")
        book = find_book(library, book_id)

        user.borrow(book)

    except Exception as e:
        print(f"Error: {e}")


def return_book_process(user):
    try:
        if not user.borrowed_books:
            print("You have no borrowed books.")
            return

        print("\nYour borrowed books:")

        for book in user.borrowed_books:
            print(f"{book.book_id} - {book.title}")

        book_id = get_integer("Enter Book ID to return: ")

        book = None

        for borrowed_book in user.borrowed_books:
            if borrowed_book.book_id == book_id:
                book = borrowed_book
                break

        if book is None:
            raise Exception("You did not borrow this book.")

        user.return_book(book)

    except Exception as e:
        print(f"Error: {e}")


def choose_user():
    while True:
        print("\n===== Smart Library Management System =====")
        print("1. Student")
        print("2. Teacher")
        print("3. Librarian")
        print("4. Exit")

        try:
            choice = int(input("Choose user type: "))

            if choice == 1:
                user_id = get_integer("Enter Student ID: ")
                name = input("Enter Student Name: ").strip()

                if not name:
                    print("Name cannot be empty.")
                    continue

                return Student(user_id, name)

            elif choice == 2:
                user_id = get_integer("Enter Teacher ID: ")
                name = input("Enter Teacher Name: ").strip()

                if not name:
                    print("Name cannot be empty.")
                    continue

                return Teacher(user_id, name)

            elif choice == 3:
                user_id = get_integer("Enter Librarian ID: ")
                name = input("Enter Librarian Name: ").strip()

                if not name:
                    print("Name cannot be empty.")
                    continue

                return Librarian(user_id, name)

            elif choice == 4:
                return None

            else:
                print("Invalid menu choice.")

        except ValueError:
            print("Invalid numeric input.")


def student_teacher_menu(user, library):
    while True:
        user.show_menu()

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                display_all_books(library)

            elif choice == 2:
                borrow_book_process(user, library)

            elif choice == 3:
                return_book_process(user)

            elif choice == 4:
                display_available_books(library)

            elif choice == 5:
                if user.borrowed_books:
                    print("\n===== Your Borrowed Books =====")

                    for book in user.borrowed_books:
                        book.display_info()
                else:
                    print("\nYou have no borrowed books.")

            elif choice == 6:
                print("Exiting...")
                break

            else:
                print("Invalid menu choice.")

        except ValueError:
            print("Invalid numeric input.")


def librarian_menu(librarian, library):
    while True:
        librarian.show_menu()

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                add_book_process(librarian, library)

            elif choice == 2:
                remove_book_process(librarian, library)

            elif choice == 3:
                search_book_process(librarian, library)

            elif choice == 4:
                display_all_books(library)

            elif choice == 5:
                borrow_book_process(librarian, library)

            elif choice == 6:
                return_book_process(librarian)

            elif choice == 7:
                display_available_books(library)

            elif choice == 8:
                display_borrowed_books(library)

            elif choice == 9:
                print("Exiting...")
                break

            else:
                print("Invalid menu choice.")

        except ValueError:
            print("Invalid numeric input.")


def main():
    library = [
        Book(1, "Python Basics", "John Smith", "Programming", 3),
        Book(2, "Database Systems", "Robert Brown", "Database", 2),
        Book(3, "Clean Code", "Robert Martin", "Programming", 4),
        Book(4, "Computer Networks", "Andrew Tanenbaum", "Networking", 2)
    ]

    user = choose_user()

    if user is None:
        print("Goodbye!")
        return

    print(f"\nWelcome, {user.name}!")

    if isinstance(user, Librarian):
        librarian_menu(user, library)
    else:
        student_teacher_menu(user, library)


if __name__ == "__main__":
    main()