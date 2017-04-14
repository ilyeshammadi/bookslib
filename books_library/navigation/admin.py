from django.contrib import admin

from .models import Search, BookHistory, History

# Register your models here.
admin.site.register(Search)
admin.site.register(BookHistory)
admin.site.register(History)
