from django.contrib import admin

from .models import Search, BookHistory

# Register your models here.
admin.site.register(Search)
admin.site.register(BookHistory)