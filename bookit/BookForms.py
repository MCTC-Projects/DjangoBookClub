from django import forms



class LoginForm(forms.Form):
    email_address = forms.EmailField()
    password = forms.PasswordInput()



class RegistrationForm(forms.Form):
    first_name = forms.CharField()
    BookClub = forms.ChoiceField()
    email_address = forms.EmailField()
    password = forms.PasswordInput()
    password_again = forms.PasswordInput()


class NewBookClubForm(forms.Form):
    bookclubname = forms.CharField()
    email_address = forms.EmailField()
    first_name = forms.CharField()
    password = forms.PasswordInput()
    password_again = forms.PasswordInput()