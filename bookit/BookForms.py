from django.forms import ModelForm
from django import forms
from registration.forms import RegistrationFormUniqueEmail


class BookClubRegistration(RegistrationFormUniqueEmail):
    bookclub_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    bookclub_description = forms.TextInput(widget=forms.Textarea(attrs={'class':'form-control'}))








