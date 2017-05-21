# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^follow/(?P<username_to_follow>\S+)$',
        view=views.follow,
        name='follow'
    ),
    url(
        regex=r'^unfollow/(?P<username_to_unfollow>\S+)$',
        view=views.unfollow,
        name='unfollow'
    ),
    url(
        regex=r'^twitter_add$',
        view=views.add_twitter_data,
        name='twitter_add'
    ),
    url(
        regex=r'^twitter_remove$',
        view=views.remove_twitter_data,
        name='twitter_remove'
    ),
    url(
        regex=r'^topics',
        view=views.topics,
        name='topics'
    ),
]
