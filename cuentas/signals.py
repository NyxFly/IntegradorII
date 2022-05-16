from email.headerregistry import Group
from unicodedata import name
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Cliente
from django.contrib.auth.models import Group

def cliente_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='clientes')
        instance.groups.add(group)

        Cliente.objects.create(
                user=instance,
                name=instance.username,   
            )
        print('Cuenta creada')
post_save.connect(cliente_profile, sender=User)