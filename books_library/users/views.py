# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import sys

from books_library.books.models import Category

reload(sys)
sys.setdefaultencoding('utf-8')

from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver

from allauth.account.signals import email_confirmed


from books_library.navigation.models import BookHistory, SocialData
from books_library.users.forms import UpdateProfileForm
from books_library.users.social import get_tweets
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
        books = user.history.books_action.filter(read=True)

        # Get all the bookmarks
        bookmarks = user.history.books_action.filter(bookmarked=True)

        # Get the following users
        following = user.following.all()

        # Get the followers users
        followers = User.objects.filter(following__username=user.username)

        # Bundle data into the context
        context['books'] = books
        context['bookmarks'] = bookmarks
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

        # If the user has choosed topics
        if self.request.user.history.has_chosed_topics:
            return reverse('suggestion')
        else:
            return reverse('users:topics')

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

@login_required
def unfollow(request, username_to_unfollow):
    """View that is used to let the login user to unfollow another user"""
    try:
        # If the logged in user is following the user to unfollow
        if request.user.following.filter(username=username_to_unfollow).exists():
            user_to_unfollow = get_object_or_404(User, username=username_to_unfollow)
            request.user.following.remove(user_to_unfollow)
            return JsonResponse({'message':'success'})
        else:
            res = JsonResponse({'message': "can't unfollow this user"})
            res.status_code = 400
            return res
    except:
        res = JsonResponse({'message': 'error'})
        res.status_code = 400
        return res

@login_required
def add_twitter_data(request):

    user = request.user
    username = request.user.username
    provider = 'twitter'

    # Check if the user has not added twitter data before
    if user.history.social_data.filter(provider=provider).exists():
        messages.error(request, 'You already added twitter data')
        return redirect('users:update')

    # Check if user is logged in with a twitter account
    has_twitter_account = SocialAccount.objects.filter(user=request.user, provider=provider).exists()
    if not has_twitter_account:
        messages.error(request, 'You are not logged in with your twitter account')
        return redirect('users:update')

    else:
        # Get the twitter
        corpus = []
        for tweet in get_tweets(username):
            tweet = tweet.decode('utf-8').strip()
            corpus.append(tweet)

        corpus = ''.join(corpus)

        social_data = SocialData(corpus=corpus, provider=provider)
        social_data.save()

        user.history.social_data.add(social_data)


    return redirect('users:update')

@login_required
def remove_twitter_data(request):
    user = request.user
    provider = 'twitter'

    # If user has a twitter social data
    has_social_data = user.history.social_data.filter(provider=provider).exists()
    if has_social_data:
        social_data = user.history.social_data.get(provider=provider)
        social_data.delete()
        messages.info(request, 'Twitter data removed from your profile')
        return redirect('users:update')
    else:
        messages.error(request, 'You dont have a twitter data asociated with your account')
        return redirect('users:update')


@login_required
def topics(request):
    # If has choosed topics before
    if request.user.history.has_chosed_topics:
        return redirect('suggestion')
    else:
        request.user.history.has_chosed_topics = True
        request.user.history.save()
        categories = Category.objects.all()
        return render(request, 'users/topics.html', {'categories' : categories})

@receiver(email_confirmed)
def email_confirmed(email_address, **kwargs):
    # Should redirect to choose topics
    return redirect('users:topics')
