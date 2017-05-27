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
        fields = ('id','slug','name', 'description', 'author','categories', 'link_to_pdf','get_thulbnail','comments', 'get_comments_count', 'get_likes_count')


class BookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','name', 'slug')
