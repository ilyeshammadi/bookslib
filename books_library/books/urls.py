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
    url(
        regex=r'^search_terms/(?P<search_terms>.+)$',
        view=views.search_terms,
        name='search_terms'
    ),
    url(
        regex=r'^search/(?P<category_slug>\S+)/(?P<search_terms>.+)$',
        view=views.index,
        name='search'
    ),
    url(
        regex=r'^search/(?P<category_slug>\S+)$',
        view=views.index,
        name='search'
    ),
    url(
        regex=r'^read/(?P<slug>\S+)$',
        view=views.book_read,
        name='read'
    ),
    url(
        regex=r'^like/(?P<id>\d+)$',
        view=views.book_like,
        name='book_like'
    ),
    url(
        regex=r'^dislike/(?P<id>\d+)$',
        view=views.book_dislike,
        name='book_dislike'
    ),
    url(
        regex=r'^bookmark/(?P<id>\d+)$',
        view=views.book_bookmark,
        name='book_bookmark'
    ),
    url(
        regex=r'^share/(?P<id>\d+)$',
        view=views.book_share,
        name='book_share'
    ),
    url(
        regex=r'^unbookmark/(?P<id>\d+)$',
        view=views.book_unbookmark,
        name='book_unbookmark'
    ),
    url(
        regex=r'^comment/$',
        view=views.add_comment,
        name='add_comment'
    ),
]
