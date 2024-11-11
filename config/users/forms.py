from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    name = forms.CharField(max_length=62)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username','name', 'email', 'password1', 'password2')
        
        