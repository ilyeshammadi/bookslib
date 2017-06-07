from django.contrib import admin

# Register your models here.
from books_library.recomendation.models import Recommender

admin.site.register(Recommender)
