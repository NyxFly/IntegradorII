from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(views_func):
    def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect('home')
            else:
                return views_func(request,*args,**kwargs)

    return wrapper_func

def allow_users(allowed_roles=[]):
    def decorator(views_func):
        def wrapper_func(request, *args, **kwargs):
                group = None
                if request.user.groups.exists():
                    group = request.user.groups.all()[0].name
                if group in allowed_roles: 
                    return views_func(request, *args, **kwargs)
                else:
                    return HttpResponse('No estas autorizado para esta pagina')
        return wrapper_func
    return decorator 


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group =='clientes':
            return redirect('user-page')
        if group == 'profesores':
            return redirect('user-page')
        if group == 'alumnos':
            return redirect('user-page')
        if group == 'en_espera':
            return redirect('en_espera')
        if group =='admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function 