# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.index,
        name='index'
    ),
url(
        regex=r'^(?P<id>\d+)$',
        view=views.detail,
        name='detail'
    ),
]
