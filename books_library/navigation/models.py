from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from books_library.books.models import Book, Category


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
    bookmarked = models.BooleanField(default=False)

    # Score as a private variable
    sc = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    @property
    def score(self):
        """
            Getter for the sc field
            >>> model.score
            # 2
        """
        return self.sc

    @score.setter
    def score(self, score):
        """
            Setter for the sc field
            >>> model.score = 2
        """
        if 0 < score and score <= 10:
            self.sc = score

    def __str__(self):
        return "id: {0} book: {1}".format(self.id, self.book.slug)

TWITTER = 'twitter'
FACEBOOK = 'facebook'
LINKEDIN = 'linkedin'
PROVIDERS = [(TWITTER, TWITTER), (FACEBOOK, FACEBOOK), (LINKEDIN, LINKEDIN)]

class SocialData(models.Model):
    provider = models.CharField(choices=PROVIDERS,max_length=50)
    corpus = models.TextField()

    def __str__(self):
        return 'id: {0}, corpus: {1}'.format(self.id, self.corpus[:30])


class Notification(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    link = models.URLField()
    viewed = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{0}'.format(self.content)

class History(models.Model):
    searchs = models.ManyToManyField(Search)
    books_action = models.ManyToManyField(BookHistory)
    social_data = models.ManyToManyField(SocialData)
    notifications = models.ManyToManyField(Notification)

    preferd_topics = models.ManyToManyField(Category)

    has_chosed_topics = models.BooleanField(default=False)

    def __str__(self):
        return 'History id: {0}'.format(self.id)
