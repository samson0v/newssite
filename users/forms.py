from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    username = forms.CharField(max_length=100)

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'birth_date', 'username', 'email', 'password1', 'password2')
        unique_together = ('email')
