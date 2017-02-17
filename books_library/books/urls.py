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
        regex=r'^detail/(?P<slug>\S+)/$',
        view=views.BookDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^create/$',
        view=views.BookCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^update/(?P<slug>\S+)/$',
        view=views.BookUpdateView.as_view(),
        name='update'
    ),
]
