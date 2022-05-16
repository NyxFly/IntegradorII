from contextlib import nullcontext
import email
from tokenize import blank_re
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    profile_pic= models.ImageField(default="profile1.png",null=True, blank= True)
    data_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Etiqueta(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Producto(models.Model):
    CATEGORY = (
                ('Indoor','Indoor'),
                ('Out Door','Out Door'),
                )
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True, choices=CATEGORY)
    description=models.CharField(max_length=200,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    etiquetas = models.ManyToManyField(Etiqueta)
    def __str__(self):
        return self.name


class Orden(models.Model):
    STATUS = (
            ('Pending','Pending'),
            ('Out for delivery','Out for delivery'),
            ('Delivered','Delivered'),
            )
    cliente= models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    producto= models.ForeignKey(Producto, null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True, choices=STATUS)
    def __str__(self):
        return self.producto.name

class Curso(models.Model):
    CAT = (
        ('Matematicas','Matematicas'),
        ('Ciencias','Ciencias'),
        ('Humanidades','Humanidades'),
        )
    name=models.CharField(max_length=200,null=True)
    horario=models.CharField(max_length=200,null=True)
    categoria = models.CharField(max_length=200, null=True, choices=CAT)
    def __str__(self):
        return self.name
class Aula(models.Model):
    opcion1 = (('1°','1°'),
                ('2°','2°'),
                ('3°','3°'),
                ('4°','4°'),
                ('5°','5°'))
    opcion2 = (('Primaria','Primaria'),
                ('Secundaria','Secundaria'))
    grado = models.CharField(max_length=200,null=True, choices=opcion1)
    año = models.CharField(max_length=200,null=True, choices=opcion2)
    seccion = models.CharField(max_length=10, null=True)
    salon = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.salon  
class Cursando(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL)
    aula = models.ForeignKey(Aula, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.cliente

    