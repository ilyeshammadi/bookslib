from rest_framework import viewsets, filters

from books_library.books.apis.paginators import BookSearchSetPagination
from .serializers import BookSerializer, CommentSerializer, CategorySerializer, BookSearchSerializer
from ..models import Book, Comment, Category


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookSearchViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSearchSerializer
    pagination_class = BookSearchSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '$name')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
