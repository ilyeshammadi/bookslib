from django.contrib import admin

from .models import Search, BookHistory, History, SocialData, Notification

# Register your models here.
admin.site.register(Search)
admin.site.register(BookHistory)
admin.site.register(SocialData)
admin.site.register(Notification)
admin.site.register(History)

