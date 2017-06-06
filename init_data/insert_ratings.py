from random import randint


from books_library.books.models import Book
from books_library.users.models import User
from books_library.navigation.models import BookHistory



users = User.objects.all()
books = Book.objects.all()[:100]


for user in users:
    for book in books:

        if user.history.books_action.filter(book=book).exists():
            book_actions = user.history.books_action.get(book=book)
            book_actions.score = randint(1, 8)
            book_actions.save()
        else:
            book_actions = BookHistory(book=book, score=randint(1, 8))
            book_actions.save()
            user.history.books_action.add(book_actions)
