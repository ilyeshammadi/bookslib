from rest_framework import viewsets

from .serializers import BookSerializer, CommentSerializer
from ..models import Book, Comment


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
