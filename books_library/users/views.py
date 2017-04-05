# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from books_library.navigation.models import BookHistory
from books_library.users.forms import UpdateProfileForm
from .models import User


class UserDetailView(DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = context['object']

        # Get all the books that the user has read
        books = BookHistory.objects.filter(user=user)

        # Get the following users
        following = user.following.all()

        # Get the followers users
        followers = User.objects.filter(following__username=user.username)

        # Bundle data into the context
        context['books'] = books
        context['following'] = following
        context['followers'] = followers

        # Check if the user is following the requested profile detail
        if self.request.user.is_authenticated():

            # Get the logged in user
            logged_in_user = self.request.user

            # If it's not the logged in user profile
            if logged_in_user != user:

                # True if the requested user is in the following
                # list of the logged in user
                context['is_following'] = user in logged_in_user.following.all()

        return context

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    form_class = UpdateProfileForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record and the profile image for the user making the request
        return User.objects.get(
            username=self.request.user.username
        )


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


@login_required
def follow(request, username_to_follow):
    """View that is used to let the login user to follow another user"""
    try:
        # If the user is not all ready begin follwed
        if not request.user.following.filter(username=username_to_follow).exists():
            user_to_follow = get_object_or_404(User, username=username_to_follow)
            request.user.following.add(user_to_follow)
            return JsonResponse({'message':'success'})
        else:
            return JsonResponse({'message': 'user is all ready being follwed'})
    except:
        res = JsonResponse({'message': 'error'})
        res.status_code = 400
        return res
