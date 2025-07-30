#problem : access contol in library system 

from dbm.ndbm import library


class User:
    def __init__(self, name):
        self.name = name
        
    def get_role(self):
        raise NotImplementedError("Subclasses should implement this method")
    
class Librarian(User):
    def get_role(self):
        return "Librarian"
    
    def add_book(self, book, library):
        library.append(book)
        print(f"{self.name} added {book.title} to the library.")

class Member(User):
    def get_role(self):
        return "Member"
    
    def borrow_book(self, book, library):
        if book in library:
            library.remove(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is not available in the library.")


def run_library_system():
    library = ["The Great Gatsby", "Moby Dick", "War and Peace"]
    
    # Create users
    users = [Librarian("Alice"), Member("Bob")]

    for user in users:
        print(f"{user.name} is a {user.get_role()}.")

        if user.get_role() == "Librarian":
            user.add_book("1984", library)
        elif user.get_role() == "Member":
            user.borrow_book("Moby Dick", library)

