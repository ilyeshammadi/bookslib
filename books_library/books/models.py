from __future__ import unicode_literals
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


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    link_to_pdf = models.URLField()
    thumbnail = models.ImageField(upload_to='books-thumbnail/', default='books-thumbnail/default.jpg')

    tags = TaggableManager()

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('books:detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('books:update', args=(self.slug,))
