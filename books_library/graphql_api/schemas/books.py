from graphene import relay, ObjectType, Schema, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from books_library.books.models import Book, Category


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (relay.Node,)


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        exclude_fields = ['language', 'tags']
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)
