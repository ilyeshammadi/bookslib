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

    liked = serializers.SerializerMethodField()
    bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
        'id', 'slug', 'name', 'description', 'author', 'categories', 'link_to_pdf', 'get_thulbnail', 'comments',
        'get_comments_count', 'get_likes_count', 'liked', 'bookmarked')

    def get_liked(self, obj):
        user = self.context['request'].user
        return user.history.books_action.filter(book=obj, liked=True).exists()

    def get_bookmarked(self, obj):
        user = self.context['request'].user
        return user.history.books_action.filter(book=obj, bookmarked=True).exists()


class BookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'slug')

class BookSimilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'slug', 'get_thulbnail')
