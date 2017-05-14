from django.contrib import admin
from django import forms
from .models import Book, Category, Comment


class BookAdminForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_display = ['id', 'name', 'slug', 'created', 'last_updated', 'link_to_pdf', 'thumbnail']
    exclude = ['language']


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Comment)
