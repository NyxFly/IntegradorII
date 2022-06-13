from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from cuentas.models import *
from django.contrib.auth import authenticate

class CreateUserForm(UserCreationForm):

    email = forms.EmailField(max_length=60,help_text='Requiere un email valido')
    class Meta:
        model = Account
        fields = {"email","username","password1","password2"}


class LoginForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = {'email','password'}
    
    def clean(self):
        email =self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Login Invalido")

class AlumnoFormConf(ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre','apellido_p','apellido_m','celular','profile_pic']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_p': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_m': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class':'form-control'}),
        }

class ProfesorFormConf(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre','apellido_p','apellido_m','celular','profile_pic']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_p': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_m': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class':'form-control'}),
        }

class ProfeCursoForm(ModelForm):
    class Meta:
        model = Aula_Curso
        fields = '__all__'
        widgets = {
        }

class ProfeCursoEditForm(ModelForm):
    class Meta:
        model = Aula_Curso
        fields = '__all__'
        exclude = ['profesor']
        widgets = {
        }

class CursoForm(ModelForm):
    class Meta:
        model= Curso
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }

class AulaAlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['aula']

class AgregarNotaForm(ModelForm):
    class Meta:
        model =Alumno_Calificaciones
        fields = '__all__'
        widgets = {
        }

class EditarNotaForm(ModelForm):
    class Meta:
        model = Alumno_Calificaciones
        fields = ['notas','trimeste']