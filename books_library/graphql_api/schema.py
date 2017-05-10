import graphene
from graphene import relay, ObjectType, Schema, AbstractType
from graphene_django.filter import DjangoFilterConnectionField


from .schemas.users import UserNode
from .schemas.books import BookNode, CategoryNode
from .schemas.navigation import SearchNode, BookHistoryNode, HistoryNode

class Query(ObjectType):
    # User
    user = graphene.Field(UserNode, id=graphene.Int())
    all_users = DjangoFilterConnectionField(UserNode)

    # Category
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    # Book
    book = graphene.Field(BookNode, id=graphene.Int())
    all_books = DjangoFilterConnectionField(BookNode)

    # Search
    search = relay.Node.Field(SearchNode)
    all_searchs = DjangoFilterConnectionField(SearchNode)

    # Book History
    book_history = graphene.Field(BookHistoryNode, id=graphene.Int())
    all_books_history = DjangoFilterConnectionField(BookHistoryNode)

    # History
    history = relay.Node.Field(HistoryNode)
    all_history = DjangoFilterConnectionField(HistoryNode)


    def resolve_user(self, args, context, info):
        query = UserNode.get_node(args.get('id'), context, info)
        return query

    def resolve_book(self, args, context, info):
        query = BookNode.get_node(args.get('id'), context, info)
        return query

    def resolve_book_history(self, args, context, info):
        query = BookHistoryNode.get_node(args.get('id'), context, info)
        return query

schema = Schema(query=Query)
