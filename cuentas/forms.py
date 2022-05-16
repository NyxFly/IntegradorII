from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class OrdenForm(ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente 
        fields = ['name','phone','email','profile_pic']