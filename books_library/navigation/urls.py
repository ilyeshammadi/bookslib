# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import notification_viewed


urlpatterns = [
    url(r'^notification/viewed/(?P<noti_id>\d+)/$', view=notification_viewed, name='notification_viewed'),
]
