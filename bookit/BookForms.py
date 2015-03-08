from django.forms import ModelForm
from django import forms
from bookit.models import Book, BookClub, Review, User



class BookClubRegistration(ModelForm):
    class Meta:
        model = BookClub
        fields = ['']


class UserLogin(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email_address']



