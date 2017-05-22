from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from books_library.books.models import Category
from books_library.navigation.models import Notification


@login_required
def notification_viewed(request, noti_id):
    try:
        user = request.user

        notification = user.history.notifications.get(pk=noti_id)
        notification.viewed = True
        notification.save()

        res = JsonResponse({'status': 'success'})
        return res
    except:
        res = JsonResponse({'status': 'error'})
        res.status_code = 400
        return res


@login_required
def add_topics(request):
    if request.method == 'POST':

        topic_ids = request.POST.get('topic_ids')
        ids = topic_ids.split('-')

        # Save each pref
        for id in ids:
            cat = Category.objects.get(pk=id)
            request.user.history.preferd_topics.add(cat)

        # User has made his pref
        request.user.history.has_chosed_topics = True
        request.user.history.save()

        return redirect('books:index')

    else:
        messages.error(request, 'Error')
        return redirect('users:topics')
