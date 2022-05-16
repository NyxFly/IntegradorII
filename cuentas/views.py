from dataclasses import fields
from http import client
from lzma import FORMAT_ALONE
from multiprocessing import context
import re
from telnetlib import LOGOUT
from tokenize import group
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .decorators import unauthenticated_user,allow_users,admin_only

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import OrdenForm, CreateUserForm, ClienteForm
from .filters import OrdenFilter
# Create your views here.

@unauthenticated_user
def registrarPage(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user =form.save()
            username = form.cleaned_data.get('username')
    
            messages.success(request,'La cuenta fue creada para '+ username)
            return redirect('login')
    context = {'form':form}
    return render(request,'cuentas/register.html',context)
@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            username= request.POST.get('username')
            password= request.POST.get('password')

            user = authenticate(request, username=username, password= password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password es incorrecto')

        context = {}
        return render(request, 'cuentas/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    orden = Orden.objects.all()
    cliente = Cliente.objects.all()
    aula = Aula.objects.all()
    total_orden =orden.count()
    
    delivered= orden.filter(status='Delivered').count()

    pending= orden.filter(status='Pending').count()

    context = {'orden':orden,'cliente':cliente,'total_orden':total_orden,'delivered':delivered,
    'pending':pending, 'aula':aula}
    return render(request, 'cuentas/dashboard.html',context)

@login_required(login_url='login')
@allow_users(allowed_roles=['alumnos'])
def paginaUsuario(request):
    cursando = request.user.cliente.cursando_set.all()
    context={'cursando':cursando}
    return render (request, 'cuentas/alumno.html',context)

@login_required(login_url='login')
@allow_users(allowed_roles=['alumnos'])
def accountSettings(request):
    clientes =request.user.cliente
    form = ClienteForm(instance=clientes)

    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=clientes)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'cuentas/account_settings.html',context)



@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def productos(request):
    productos=Producto.objects.all()
    return  render(request, 'cuentas/productos.html',{'productos':productos})

@login_required(login_url='login')
def cursos(request):
    cursos=Curso.objects.all()
    return render(request,'cuentas/cursos.html',{'cursos':cursos})


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def clientes(request,pk):
    clientes = Cliente.objects.get(id=pk)
    cursando = clientes.cursando_set.all()
    total_cursos =cursando.count()
    context= {'clientes':clientes,'cursando':cursando,'total_cursos':total_cursos}
    return  render(request, 'cuentas/clientes.html',context) 

@login_required(login_url='login')
def Aulas(request,pk):
    aula = Aula.objects.get(id=pk)
    cursando = aula.cursando_set.all()
    context = {'aula':aula,'cursando':cursando}
    return render(request, 'cuentas/aula.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def crearOrden(request,pk):
    OrdenFormSet = inlineformset_factory(Cliente, Orden, fields=('producto','status'),extra=5)
    clientes = Cliente.objects.get(id=pk)
    formset = OrdenFormSet(queryset=Orden.objects.none(),instance=clientes)
    if request.method == 'POST':
        formset = OrdenFormSet(request.POST,instance=clientes)
        if formset.is_valid():
            formset.save()
            return redirect ('/')

    context = {'formset':formset}
    return render(request,'cuentas/orden_form.html',context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def CrearEnCurso(request,pk):
    CursandoFormSet = inlineformset_factory(Cliente, Cursando, fields=('aula',), extra=1)
    clientes = Cliente.objects.get(id=pk)
    formset = CursandoFormSet(queryset=Cursando.objects.none(),instance=clientes)
    if request.method == 'POST':
        formset = CursandoFormSet(request.POST,instance=clientes)
        if formset.is_valid():
            formset.save()
            return redirect ('/')
    context = {'formset':formset}
    return render(request, 'cuentas/EncursoForm.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def AgregarCursos(request,pk):
    AgregarcursFormSet = inlineformset_factory(Cliente, Cursando, fields=('curso',), extra=3)
    clientes = Cliente.objects.get(id=pk)
    formset = AgregarcursFormSet(queryset=Cursando.objects.none(),instance=clientes)
    if request.method == 'POST':
        formset = AgregarcursFormSet(request.POST,instance=clientes)
        if formset.is_valid():
            formset.save()
            return redirect ('/')
    context = {'formset': formset}
    return render (request, 'cuentas/agregarcursos.html',context)



@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def actualizarOrden(request,pk):
    orden = Orden.objects.get(id=pk)
    form = OrdenForm(instance=orden)
    if request.method == 'POST':
        
        form = OrdenForm(request.POST,instance=orden)
        if form.is_valid():
            form.save()
            return redirect ('/')

    context = {'form':form}
    return render(request, 'cuentas/orden_form.html', context)

@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def eliminarOrden(request,pk):
    orden = Orden.objects.get(id=pk)
    if request.method == 'POST':
        orden.delete()
        return redirect('/')
    context={'orden':orden}
    return render(request,'cuentas/eliminar.html', context)
