from django import forms
from .models import CustomerUser


class EditWishEvent(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ('name', 'email', 'birth_day')
        
        
