from django.urls import reverse
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from books_library.books.apis.paginators import BookSearchSetPagination
from books_library.navigation.models import BookHistory
from books_library.navigation.sentiment import get_sentiment, POSITIVE
from books_library.recomendation.views import get_rec
from .serializers import BookSerializer, CommentSerializer, CategorySerializer, BookSearchSerializer, \
    BookSimilarSerializer
from ..models import Book, Comment, Category

from books_library.users.models import User

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        """Return the requested book and save the navigation"""
        # Get the object from the super class method
        book = super(BookViewSet, self).get_object()

        # If the user is logged in, save the book history actions
        if self.request.user.is_authenticated():

            # Get the logged in user
            user = self.request.user

            # If the user has not viewed the book, create a new BookAction model and save
            # in the user history field
            if not user.history.books_action.filter(book=book).exists():
                book_actions = BookHistory(book=book, viewed=True)
                book_actions.score += 1
                book_actions.save()
                user.history.books_action.add(book_actions)
            else:
                books_action = user.history.books_action.get(book=book)
                if not books_action.viewed:
                    books_action.viewed = True
                    books_action.score += 1
                    books_action.save()

        return book


class BookSearchViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSearchSerializer
    pagination_class = BookSearchSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '$name')

class BookSimilarViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        books = super(BookSimilarViewSet, self).get_queryset()

        try:
            book_id = self.request.GET.get('book_id')
            book_ids = get_rec(book_id)
            return books.filter(id__in=book_ids)
        except:
            return books.all()[:10]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def book_like(request, id):
    """Take the id of the book to like"""
    try:
        # Get the logged in user
        user = request.user

        # Get the Book to read
        book = Book.objects.get(pk=id)

        # If the book is in the user history
        if user.history.books_action.filter(book=book).exists():
            book_history = user.history.books_action.get(book=book)

            if not book_history.liked:
                book_history.liked = True
                book_history.score += 1
                book_history.save()

                book.likes.add(user)
                book.save()
            else:
                res = Response({'message': "Can't like a book more then one time"})
                res.status_code = 400
                return res
        else:
            book_history = BookHistory(book=book)
            book_history.liked = True
            book_history.score += 1
            book_history.save()
            user.history.books_action.add(book_history)

            # Increse the like by one
            book.likes.add(user)
            book.save()

        return Response({'message': 'book {0} is liked by the user {1}'.format(book.name, user.username),
                             'likes': book.likes.count()})

    except:
        res = Response({'message': 'error'})
        res.status_code = 400
        return res


@api_view(['GET'])
def book_dislike(request, id):
    """Take the id of the book to dislike"""
    try:
        # Get the logged in user
        user = request.user

        # Get the Book to read
        book = Book.objects.get(pk=id)

        # If the book is in the user history
        if user.history.books_action.filter(book=book).exists():
            book_history = user.history.books_action.get(book=book)

            if book_history.liked:
                book_history.liked = False
                book.likes.remove(user)
                book.save()
            else:
                res = Response({'message': "Can't dislike a book more then one time"})
                res.status_code = 400
                return res

            book_history.save()

        return Response({'message': 'book {0} is disliked by the user {1}'.format(book.name, user.username),
                             'likes': book.likes.count()})

    except:
        res = Response({'message': 'error'})
        res.status_code = 400
        return res


@api_view(['GET'])
def book_bookmark(request, id):
    """Take the id of the book to bookmark"""
    try:
        # Get the logged in user
        user = request.user

        # Get the Book to read
        book = Book.objects.get(pk=id)

        # If the book is in the user history
        if user.history.books_action.filter(book=book).exists():
            book_history = user.history.books_action.get(book=book)

            if not book_history.bookmarked:
                book_history.bookmarked = True
                book_history.score += 1
                book_history.save()

            else:
                res = Response({'message': "Can't bookmark a book more then one time"})
                res.status_code = 400
                return res
        else:
            book_history = BookHistory(book=book)
            book_history.bookmarked = True
            book_history.score += 1
            book_history.save()
            user.history.books_action.add(book_history)

        return Response({'message': 'book {0} is bookmarked by the user {1}'.format(book.name, user.username)})

    except:
        res = Response({'message': 'error'})
        res.status_code = 400
        return res

@api_view(['GET'])
def add_comment(request):
    try:
        username = request.GET.get('username')
        book_id = request.GET.get('book_id')
        comment_content = request.GET.get('comment_content')

        print('User {}'.format(username))
        print('Book {}'.format(book_id))
        print('Comment {}'.format(comment_content))

        user = User.objects.get(username=username)
        book = Book.objects.get(id=book_id)

        comment = Comment(user=user, content=comment_content)
        sentiment = get_sentiment(comment.content)
        comment.sentiment = sentiment
        comment.save()

        book.comments.add(comment)

        if sentiment == POSITIVE:
            books_action = request.user.history.books_action.get(book=book)
            books_action.score += 1
            books_action.save()

        book.comments.add(comment)

        users = User.objects.filter(history__books_action__book=book).distinct().exclude(
            username__exact=request.user.username)
        link = reverse('books:detail', kwargs={'slug': book.slug}) + '#{0}'.format(comment.id)
        content = 'has commented on {1}'.format(request.user.username, book.name)
        for user in users:
            user.notify(sender=request.user, content=content, link=link)

        return Response({'status': 'success'})
    except:
        return Response({'status': 'error'})
