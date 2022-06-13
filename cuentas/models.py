from django.conf import settings
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo")
        if not username:
            raise ValueError("El ususario debe tener un Username")

        my_user = self.model(
            email=self.normalize_email(email),
            username=username)

        my_user.set_password(password)
        my_user.save(using=self._db)
        return my_user

    def create_superuser(self, email, username, password):
        my_user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username
                )
        my_user.is_admin = True
        my_user.is_staff = True
        my_user.is_superuser = True
        my_user.save(using=self._db)
        return my_user

class Account(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(verbose_name="email", max_length=60, unique=True)
    username=models.CharField(max_length=30, unique=True)
    date_joined=models.DateTimeField(verbose_name='data joined', auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    
    objects= MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True


class Aula(models.Model):
    opcion1 = (('1°','1°'),
                ('2°','2°'),
                ('3°','3°'),
                ('4°','4°'),
                ('5°','5°'))
    opcion2 = (('Primaria','Primaria'),
                ('Secundaria','Secundaria'))
    grado = models.CharField(choices=opcion1,null=True,max_length=10)
    año = models.CharField(choices=opcion2,null=True,max_length=10)
    seccion = models.CharField(max_length=5, null=True)
    salon = models.CharField(max_length=4, null=True)
    def __str__(self):
        return self.salon 


class Curso(models.Model):
    CAT = (
        ('Matematicas','Matematicas'),
        ('Ciencias','Ciencias'),
        ('Humanidades','Humanidades'),
        )
    nombre=models.CharField(max_length=50,null=True,unique=True)
    categoria = models.CharField(max_length=50,null=True,choices=CAT)
    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    email = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,max_length=50,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50,null=True)
    apellido_p=models.CharField(max_length=50,null=True)
    apellido_m=models.CharField(max_length=50, null=True)
    celular = models.CharField(max_length=12,null=True)
    profile_pic= models.ImageField(default="profile.png",null=True, blank= True)
    data_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.nombre+" "+self.apellido_p


class Alumno(models.Model):
    email = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50,null=True)
    apellido_p=models.CharField(max_length=50,null=True)
    apellido_m=models.CharField(max_length=50,null=True)
    celular=models.CharField(max_length=12,null=True)
    aula=models.ForeignKey(Aula,on_delete=models.CASCADE,null=True,related_name='alumnos')
    profile_pic= models.ImageField(default="profile.png",null=True, blank= True)
    data_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.nombre


class Aula_Curso(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE,related_name='aula')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor,on_delete=models.CASCADE,null=True, related_name='profesor')
    horario_i = models.TimeField(max_length=10, null=True)
    horario_f = models.TimeField(max_length=10,null=True)
    dia_semana = models.CharField(max_length=12, null=True)
    def __str__(self):
        return self.aula.grado +"  "+ self.curso.nombre

class Alumno_Calificaciones(models.Model):
    alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE,null=True,related_name="estudiante")
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE,null=True,blank=True, related_name='cursos')
    notas = models.IntegerField(null=True)
    trimeste = models.CharField(max_length=10,null=True)  
    def __str__(self):
        return self.curso.nombre
