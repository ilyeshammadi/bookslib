from django import template

from books_library.navigation.sentiment import POSITIVE, NEUTRAL, NEGATIVE

register = template.Library()




@register.filter('isliked')
def isliked(book, user):
    return user in book.likes.all()

@register.filter('viewed')
def viewed(books):
    return len(books.filter(read=True))

@register.filter('hasTwitter')
def hasTwitter(user):
    return user.history.social_data.filter(provider='twitter')

@register.filter('isBookmarked')
def isBookmarked(book, user):
    return user.history.books_action.filter(book=book, bookmarked=True).exists()


@register.filter('isPositive')
def isPositive(comment):
    return comment.sentiment == POSITIVE

@register.filter('isNegative')
def isNegative(comment):
    return comment.sentiment == NEGATIVE

@register.filter('isNeutral')
def isNeutral(comment):
    return comment.sentiment == NEUTRAL

@register.filter('notViewedCounter')
def notViewedCounter(notifications):
    return len(notifications.filter(viewed=False))
