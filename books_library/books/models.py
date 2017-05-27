from __future__ import unicode_literals

import json

import requests
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields

from languages.fields import LanguageField

from books_library.navigation.sentiment import NEUTRAL, NEGATIVE, POSITIVE

choices = [(POSITIVE, POSITIVE), (NEGATIVE, NEGATIVE), (NEUTRAL, NEUTRAL)]


class Category(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    image = models.ImageField(upload_to='categories/')

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    sentiment = models.CharField(max_length=50, choices=choices, default=choices[2][0])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{0} -- {1}".format(self.user, self.content[:20])


class Book(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='no-author')
    description = models.TextField()

    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    link_to_pdf = models.URLField()
    thumbnail = models.ImageField(
        upload_to='books-thumbnail/', default='books-thumbnail/default.jpg')

    thumbnail_url = models.URLField(blank=True, null=True)

    publication_date = models.DateField(null=True, blank=True)

    # The city and country where the book was published
    publication_place = models.CharField(max_length=120, null=True, blank=True)

    publisher = models.CharField(max_length=120, null=True, blank=True)
    language = LanguageField(null=True, blank=True)

    isbn10 = models.CharField(max_length=250, null=True, blank=True)
    isbn13 = models.CharField(max_length=250, null=True, blank=True)

    tags = TaggableManager()

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    likes = models.ManyToManyField('users.User', blank=True)

    # Relationship Fields
    categories = models.ForeignKey(Category)

    # Comments
    comments = models.ManyToManyField(Comment, blank=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('books:detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('books:update', args=(self.slug,))


    def get_thulbnail(self):
        if self.thumbnail_url:
            return self.thumbnail_url
        elif self.thumbnail:
            return self.thumbnail
        else:
            return None

    def get_comments_count(self):
        if(self.comments.all() > 0):
            return len(self.comments.all())
        else:
            return 0

    def get_likes_count(self):
        if(self.likes.all() > 0):
            return len(self.likes.all())
        else:
            return 0
