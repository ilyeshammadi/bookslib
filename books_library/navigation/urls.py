# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import notification_viewed, add_topics



urlpatterns = [
    url(r'^notification/viewed/(?P<noti_id>\d+)/$', view=notification_viewed, name='notification_viewed'),
    url(r'^topics_add/$', csrf_exempt(add_topics), name='topic_add')
]
