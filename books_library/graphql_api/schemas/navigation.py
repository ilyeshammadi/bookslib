import graphene
from graphene import relay, ObjectType, Schema, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from books_library.navigation.models import Search, BookHistory, History, SocialData


class SearchNode(DjangoObjectType):
    class Meta:
        model = Search
        interfaces = (relay.Node,)

    pk = graphene.Int()

class BookHistoryNode(DjangoObjectType):
    class Meta:
        model = BookHistory
        interfaces = (relay.Node,)

    pk = graphene.Int()

class SocialDataNode(DjangoObjectType):
    class Meta:
        model = SocialData
        interfaces = (relay.Node,)

    pk = graphene.Int()

class HistoryNode(DjangoObjectType):
    class Meta:
        model = History
        interfaces = (relay.Node, )

    pk = graphene.Int()
