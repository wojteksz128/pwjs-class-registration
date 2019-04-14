from django import forms
from .models import Subject

class RegisterForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    album_no = forms.IntegerField(min_value=0)