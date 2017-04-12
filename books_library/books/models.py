from __future__ import unicode_literals

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

class Category(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug


class Book(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=80, default='no-author')
    description = models.TextField()

    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    link_to_pdf = models.URLField()
    thumbnail = models.ImageField(
        upload_to='books-thumbnail/', default='books-thumbnail/default.jpg')

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


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('books:detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('books:update', args=(self.slug,))
