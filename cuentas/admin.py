from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cuentas.models import *


class AccountAdmin(UserAdmin):
    list_display = ('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal= ()
    list_filter= ()
    fieldsets =()

class AulaAdmin(admin.ModelAdmin):
    list_display = ('grado', 'año','seccion','salon')

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria')

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','apellido_p','apellido_m','celular','email')

class Aula_CursoAdmin(admin.ModelAdmin):
    list_display = ('aula','curso','profesor','horario_i','horario_f')

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','apellido_p','apellido_m','celular','aula')

class CalificacionesAdmin(admin.ModelAdmin):
    list_display = ('id','alumno','notas',"trimeste",'curso')



admin.site.register(Account,AccountAdmin)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Aula,AulaAdmin)
admin.site.register(Aula_Curso,Aula_CursoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Alumno_Calificaciones,CalificacionesAdmin)

