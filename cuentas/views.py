from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from cuentas.forms import *
from cuentas.models import Alumno, Aula, Aula_Curso, Curso, Profesor
from .decorators import unauthenticated_user,allow_users,admin_only
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory

@unauthenticated_user
def registrarPage(request):
    form =CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request,'La cuenta fue creada para: '+  email)
            return redirect ('login')

    context={'form_registrar':form}
    return render(request, 'cuentas/registrar.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request,user)
                return redirect ('home')
            else:
                messages.info(request,'Email o contraseña es incorrecta')
    context={}
    return render (request,'cuentas/login.html',context)


def logoutPage(request):
    logout(request)
    return redirect ('login')


@login_required(login_url='login')
@admin_only
def home(request):
    profe=Profesor.objects.all()
    aula = Aula.objects.all()
    context={'profe':profe,'aula':aula}
    return render (request, 'cuentas/dashboard.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['alumnos','profesores'])
def paginaUsuario(request):
    context={}
    return render (request,'cuentas/alumno.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['alumnos'])
def confPerfAlumno(request):
    alum = request.user.alumno
    a_form = AlumnoFormConf(instance=alum)
    if request.method == 'POST':
        a_form = AlumnoFormConf(request.POST,request.FILES, instance=alum)
        if a_form.is_valid():
            a_form.save()
    context= {'a_form':a_form}
    return render (request, 'cuentas/confPerfAlumno.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['profesores'])
def confPerfProfesor(request):
    profe = request.user.profesor
    pf_form = ProfesorFormConf(instance=profe)
    if request.method == 'POST':
        pf_form = ProfesorFormConf(request.POST, request.FILES, instance=profe)
        if pf_form.is_valid():
            pf_form.save()
    
    context = {'pf_form':pf_form}
    return render (request,'cuentas/confPerfProfesor.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def ViewProfesorAdmin(request,pk):
    profe = Profesor.objects.get(id=pk)
    prof_curs= profe.profesor.all().order_by("horario_i","horario_f","dia_semana")
    total_curso = prof_curs.count()
    context={'profe':profe,'prof_curs':prof_curs,'total_curso':total_curso}
    return render (request,'cuentas/profesor.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def Asignar_ProfeCurs(request):
    form_pfcr= ProfeCursoForm()
    if request.method =='POST':
        form_pfcr= ProfeCursoForm(request.POST)
        if form_pfcr.is_valid():
            form_pfcr.save()
            return redirect ('/')
    context = {'form_pfcr':form_pfcr}
    return render (request,'cuentas/asignar_profcurso.html', context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def Editar_ProfeCurs(request,pk):
    aula_curs = Aula_Curso.objects.get(id=pk)
    form_pc = ProfeCursoEditForm (instance=aula_curs)
    if request.method == 'POST':
        form_pc = ProfeCursoEditForm(request.POST, instance=aula_curs)
        if form_pc.is_valid():
            form_pc.save()
            return redirect ('/')
    context ={'form_pc':form_pc}
    return render (request,'cuentas/editar_profcurso.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def Eliminar_ProfeCurs(request,pk):
    aula_curso = Aula_Curso.objects.get(id=pk)
    if request.method == 'POST':
        aula_curso.delete()
        return redirect ('/')
    context ={'aula_curso':aula_curso}
    return render (request,'cuentas/eliminar_profcurso.html',context)



@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def ViewAulas_AlumnoAula(request,pk):
    aula = Aula.objects.get(id=pk)
    alumno = aula.alumnos.all()
    context = {'aula':aula,'alumno':alumno}
    return render (request,'cuentas/aula.html',context)


@login_required(login_url='login')
def ViewEn_Espera(request):
    if request.method == 'POST':
        mensaje = request.POST['mensaje']
        send_mail(
            'Informacion del Alumno/Profesor',
            mensaje,
            settings.EMAIL_HOST_USER,
            ['templance.25.94@gmail.com'],
            fail_silently=False)
        messages.success(request,'El mensaje a sido Enviado correctamente')
    return render(request,'cuentas/en_espera.html')


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def Asignar_AlumnAula(request,pk):
    alumno = Alumno.objects.get(id=pk)
    aula_form = AulaAlumnoForm(instance=alumno)
    if request.method == 'POST':
        aula_form = AulaAlumnoForm(request.POST, instance=alumno)
        if aula_form.is_valid():
            aula_form.save()
            return redirect ('total_alumnos')
    context = {'aula_form':aula_form,'alumno':alumno}
    return render (request, 'cuentas/asignar_alumno.html', context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def View_AlumnosTot(request):
    alumno = Alumno.objects.all().order_by('aula')
    context = {'alumno':alumno}
    return render(request,'cuentas/total_alumnos.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def ViewCursosAdmin(request):
    curso = Curso.objects.all()
    context = {'curso':curso}
    return render (request,'cuentas/cursos.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def AgregarCurso(request):
    formc = CursoForm()
    if request.method == 'POST':
        formc = CursoForm(request.POST)
        if formc.is_valid():
            formc.save()
            messages.success(request,'El curso ha sido agregado')
            return redirect ('cursos')
    context = {'formc':formc}
    return render (request, 'cuentas/agregar_curso.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def EditarCurso(request,pk):
    curso = Curso.objects.get(id=pk)
    form_c = CursoForm(instance=curso)
    if request.method == 'POST':
        form_c = CursoForm(request.POST, instance=curso)
        if form_c.is_valid():
            form_c.save()
            messages.success(request,'El curso ha sido Modificado')
            return redirect ('cursos')
    context = {'form_c':form_c}
    return render (request,'cuentas/editar_curso.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['admin'])
def EliminarCurso(request,pk):
    curso = Curso.objects.get(id=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect ('cursos')
    context = {'curso':curso}
    return render (request, 'cuentas/eliminar_curso.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['profesores'])
def View_CursoProfesor(request, pk):
    profe = Profesor.objects.get(id=pk)
    prof_curs= profe.profesor.all().order_by("dia_semana","horario_i")
    context={'profe':profe,'prof_curs':prof_curs}
    return render (request,'cuentas/ver_PCursos.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['alumnos'])
def View_CursoAlumno(request,pk):
    aula = Aula.objects.get(id=pk)
    alumno = aula.aula.all().order_by("dia_semana","horario_i")
    context={'alumno':alumno,'aula':aula}
    return render (request, 'cuentas/ver_ACursos.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['profesores'])
def ViewP_AlumnosporCurso(request,pk,curso):
    aula = Aula.objects.get(id=pk)
    alumno= aula.alumnos.all()
    pb = curso
    context={'aula':aula,'alumno':alumno,'pb':pb}
    return render (request,'cuentas/Alumno_porCurso.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['profesores'])
def ViewP_NotasAlumnos(request,pk,curso):
    alum = Alumno_Calificaciones.objects.all().filter(alumno_id=pk, curso_id=curso).order_by('trimeste')
    alumno = Alumno.objects.get(id=pk)
    context={'alum':alum,'alumno':alumno}
    return render (request,'cuentas/verP_Notas.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['profesores'])
def View_AgregarNotas(request,pk):
    NotasFormset = inlineformset_factory(Alumno,Alumno_Calificaciones,fields=('curso','notas','trimeste',),extra=1)
    curso = Alumno.objects.get(id=pk)
    formset = NotasFormset(queryset=Alumno_Calificaciones.objects.none(),instance=curso)
    if request.method == 'POST':
        formset = NotasFormset(request.POST, instance=curso)
        if formset.is_valid():
            formset.save()
            return redirect ('home')
    context={'form':formset,'pk':pk}
    return render(request,'cuentas/agregar_nota.html',context)


@login_required(login_url='login')
@allow_users(allowed_roles=['profesores'])
def View_EditarNotas(request,pk):
    alu_cali = Alumno_Calificaciones.objects.get(id=pk)
    form_n = AgregarNotaForm(instance=alu_cali)
    if request.method == 'POST':
        form_n=AgregarNotaForm(request.POST, instance=alu_cali)
        if form_n.is_valid():
            form_n.save()
            return redirect ('home')
    context={'form_n':form_n}
    return render(request,'cuentas/editar_nota.html',context)



@login_required(login_url='login')
@allow_users(allowed_roles=['alumnos'])
def View_NotasAlumno(request,pk,cs):
    notas =Alumno_Calificaciones.objects.all().filter(alumno_id=pk,curso_id=cs)
    context={'notas':notas}
    return render (request,'cuentas/verA_Notas.html',context)
