from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from books_library.books.models import Book

# Create your models here.



class Search(models.Model):
    terms = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.terms + ' --- ' + str(self.created)


class BookHistory(models.Model):
    book = models.ForeignKey(Book)

    viewed = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    shared = models.BooleanField(default=False)
    liked = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "id: {0} book: {1}".format(self.id, self.book.slug)


class SocialData(models.Model):
    provider = models.CharField(max_length=50)
    corpus = models.TextField()

    def __str__(self):
        return 'id: {0}, corpus: {1}'.format(self.id, self.corpus[:30])


class History(models.Model):
    searchs = models.ManyToManyField(Search)
    books_action = models.ManyToManyField(BookHistory)
    social_data = models.ManyToManyField(SocialData)

    def __str__(self):
        return 'History id: {0}'.format(self.id)
