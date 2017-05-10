import graphene
from graphene import relay, ObjectType, Schema, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from books_library.users.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'username' : ['exact']
        }
        interfaces = (relay.Node,)

    pk = graphene.Int()
