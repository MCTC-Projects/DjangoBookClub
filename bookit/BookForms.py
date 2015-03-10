from django.forms import ModelForm
from django import forms
from bookit.models import Book, BookClub, Review, User



class BookClubRegistration(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = BookClub
        fields = ('bookclub_name','bookclub_description','owners_first_name','owners_email_address')


class UserLogin(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email_address',)



