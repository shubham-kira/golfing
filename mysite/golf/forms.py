from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import tournament
from django.contrib.auth.models import User

class TournamentForm(forms.ModelForm):
    class Meta:
        model = tournament
        fields = ('name', 'desc', )

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']