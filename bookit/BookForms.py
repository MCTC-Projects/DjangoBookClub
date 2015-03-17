from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm


class BookClubRegistration(UserCreationForm):
    bookclub_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    bookclub_description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))








