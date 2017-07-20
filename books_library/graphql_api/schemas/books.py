import graphene
from graphene import relay, ObjectType, Schema, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from books_library.books.models import Book, Category, Comment


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node,)

    pk = graphene.Int()

class CommentNode(DjangoObjectType):
    class Meta:
        model = Comment
        interfaces = (relay.Node,)

    pk = graphene.Int()

class BookNode(DjangoObjectType):
    pk = graphene.Int()
    class Meta:
        model = Book
        exclude_fields = ['language', 'tags']
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)


