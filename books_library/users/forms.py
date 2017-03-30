from django import forms

from books_library.users.models import User


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'image', 'bio')
