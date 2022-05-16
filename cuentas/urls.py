from cmath import nan
from re import template
from unicodedata import name
from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', views.registrarPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('alumno/',views.paginaUsuario,name="user-page"),
    path('account/',views.accountSettings,name="account"),
    path('productos/', views.productos, name="productos"),
    path('cursos/',views.cursos, name="cursos"),
    path('clientes/<str:pk>/', views.clientes, name="clientes"),
    path('aula/<str:pk>/',views.Aulas, name="aula"),
    path('crear_orden/<str:pk>',views.crearOrden, name="crear_orden"),
    path('actualizar_orden/<str:pk>',views.actualizarOrden, name="actualizar_orden"),
    path('eliminar_orden/<str:pk>',views.eliminarOrden, name="eliminar_orden"),
    path('crear_encurso/<str:pk>',views.CrearEnCurso,name="crear_encurso"),
    path('agregar_cursos/<str:pk>',views.AgregarCursos,name="agregar_cursos"),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="cuentas/password_reset.html"),
     name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="cuentas/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="cuentas/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="cuentas/password_reset_done.html"), 
        name="password_reset_complete"),
]
  