from __future__ import unicode_literals

from django.db import models

from ..users.models import User
from ..books.models import Book


# Create your models here.
class Search(models.Model):

    user = models.ForeignKey(User)
    terms = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.terms + ' --- ' + str(self.created)


class BookHistory(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)

    viewed = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    shared = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.book) + ' --- ' + str(self.user)