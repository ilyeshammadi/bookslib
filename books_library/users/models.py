# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from books_library.navigation.models import History, Notification


@python_2_unicode_compatible
class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    image = models.ImageField(upload_to='users/', default='users/default.png')
    bio = models.TextField(blank=True)

    following = models.ManyToManyField('User', related_name='user_following', blank=True)

    history = models.OneToOneField(History, null=True, blank=True)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def save(self, *args, **kwargs):
        if self.history == None:
            self.history = History.objects.create()

        super(User, self).save(*args, **kwargs)


    def notify(self, sender, content, link):
        noti = Notification(sender=sender, content=content, link=link)
        noti.save()

        self.history.notifications.add(noti)
