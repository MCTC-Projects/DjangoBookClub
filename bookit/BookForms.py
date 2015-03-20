from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from bookit.models import BookClub

class BookClubRegistration(UserCreationForm):
    bookclub_name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    bookclub_description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        labels = {'username': ('email',),
                  }




