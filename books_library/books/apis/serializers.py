from rest_framework import serializers

from books_library.users.apis.serializers import UserSerializer
from ..models import Book, Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('user', 'content', 'sentiment')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Book
        fields = ('name', 'description', 'author', 'get_thulbnail', 'comments')
