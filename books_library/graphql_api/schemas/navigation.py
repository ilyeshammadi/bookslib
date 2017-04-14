from graphene import relay, ObjectType, Schema, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from books_library.navigation.models import Search, BookHistory, History


class SearchNode(DjangoObjectType):
    class Meta:
        model = Search
        interfaces = (relay.Node,)


class BookHistoryNode(DjangoObjectType):
    class Meta:
        model = BookHistory
        interfaces = (relay.Node,)


class HistoryNode(DjangoObjectType):
    class Meta:
        model = History
        interfaces = (relay.Node, )
