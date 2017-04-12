from graphene import relay, ObjectType, Schema, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from books_library.navigation.models import Search, BookHistory


class SearchNode(DjangoObjectType):
    class Meta:
        model = Search
        interfaces = (relay.Node,)


class BookHistoryNode(DjangoObjectType):
    class Meta:
        model = Search
        interfaces = (relay.Node,)



