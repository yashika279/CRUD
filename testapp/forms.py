from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User
from testapp.models import Insertion
class InsertionForm(forms.ModelForm):
    class Meta:
        model=Insertion
        fields='__all__'