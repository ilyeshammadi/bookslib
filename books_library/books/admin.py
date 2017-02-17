from django.contrib import admin
from django import forms
from .models import Book

class BookAdminForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'link_to_pdf', 'thumbnail']

admin.site.register(Book, BookAdmin)
