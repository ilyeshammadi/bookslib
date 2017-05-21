from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from books_library.navigation.models import Notification

@login_required
def notification_viewed(request, noti_id):
    try:
        user = request.user

        notification = user.history.notifications.get(pk=noti_id)
        notification.viewed = True
        notification.save()

        res = JsonResponse({'status' : 'success'})
        return res
    except:
        res = JsonResponse({'status': 'error'})
        res.status_code = 400
        return res
