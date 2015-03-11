from django.forms import ModelForm
from django import forms
from bookit.models import Book, BookClub, Review, User
from django.core.validators import validate_email


class BookClubRegistration(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = BookClub
        fields = ('bookclub_name','bookclub_description','owners_first_name','owners_email_address')


class UserLogin(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email_address = forms.CharField(validators=[validate_email])
    class Meta:
        model = User
        exclude = ['first_name','bookclub']






