from graphene import relay, ObjectType, Schema, AbstractType
from graphene_django.filter import DjangoFilterConnectionField


from .schemas.users import UserNode
from .schemas.books import BookNode, CategoryNode
from .schemas.navigation import SearchNode, BookHistoryNode

class Query(ObjectType):
    # User
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    # Category
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    # Book
    book = relay.Node.Field(BookNode)
    all_books = DjangoFilterConnectionField(BookNode)

    # Search
    search = relay.Node.Field(SearchNode)
    all_searchs = DjangoFilterConnectionField(SearchNode)

    # Book History
    book_history = relay.Node.Field(BookHistoryNode)
    all_books_history = DjangoFilterConnectionField(BookHistoryNode)


schema = Schema(query=Query)
