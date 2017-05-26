from rest_framework import serializers

from books_library.users.apis.serializers import UserSerializer
from ..models import Book, Comment, Category

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('user', 'content', 'sentiment')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'image')

class BookSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True)
    categories = CategorySerializer()
    class Meta:
        model = Book
        fields = ('name', 'description', 'author','categories', 'get_thulbnail','comments')


class BookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'slug')
