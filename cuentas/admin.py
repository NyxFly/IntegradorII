from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Etiqueta)
admin.site.register(Orden)
admin.site.register(Curso)
admin.site.register(Cursando)
admin.site.register(Aula)