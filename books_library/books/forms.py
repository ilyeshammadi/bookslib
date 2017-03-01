from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'description', 'link_to_pdf', 'thumbnail', 'publication_date', 'publication_place',
                  'language','tags', 'categories']
