# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from graphene_django.views import GraphQLView

from books_library.recomendation.views import suggestion
from books_library.graphql_api.schema import schema
from books_library.graphql_api.views import PrivateGraphQLView

from books_library.users.views import is_logged_in

urlpatterns = [
    url(r'^$',is_logged_in, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('books_library.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # GraphQL
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),


    # Books
    url(r'^books/', include('books_library.books.urls', namespace='books')),
    url(r'^suggestions$', suggestion, name="suggestion"),

    # Navigations
    url(r'^navigation/', include('books_library.navigation.urls', namespace="navigation")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
