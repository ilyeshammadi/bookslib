from django import template

register = template.Library()




@register.filter('isliked')
def isliked(book, user):
    return user in book.likes.all()
