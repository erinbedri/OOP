class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user):
        for a, books in self.books_available.items():
            if a == author:
                for b in books:
                    if b == book_name:
                        user.books.append(b)
                        self.books_available[a].remove(b)
                        self.rented_books[user.username] = {b: days_to_return}
                        return f"{book_name} successfully rented for the next {days_to_return} days!"

        return f'The book "{book_name}" is already rented and will be available in ' \
               f'{self.rented_books[user.username][book_name]} days!'

    def return_book(self, author, book_name, user):
        for b in user.books:
            if b == book_name:
                user.books.remove(b)
                self.books_available[author].append(b)
                del self.rented_books[user.username][b]
        return f"{user.username} doesn't have this book in his/her records!"