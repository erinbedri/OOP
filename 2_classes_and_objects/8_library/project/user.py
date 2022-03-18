from project.library import Library
from project.registration import Registration


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        sorted_books = sorted(self.books)
        return f"{(', '.join(sorted_books))}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"


user = User(12, 'Peter')
library = Library()
registration = Registration()
registration.add_user(user, library)
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})
library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user)
library.get_book('J.K.Rowling', 'The Chamber of Secrets', 143, user)
print(user.info())
