from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('registrar/', views.registrarPage, name="registrar"),
    path('login/', views.loginPage, name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('', views.home, name="home"),
    path('alumno/',views.paginaUsuario,name='user-page'),
    path('confPerfAlumno/',views.confPerfAlumno,name='confPerfAlumno'),
    path('confPerfProfesor/',views.confPerfProfesor,name='confPerfProfesor'),
    path('profesor/<str:pk>/',views.ViewProfesorAdmin,name='profesor'),
    path('asignar_profcurso/',views.Asignar_ProfeCurs,name='asignar_profcurso'),
    path('editar_profcurso/<str:pk>/',views.Editar_ProfeCurs,name='editar_profcurso'),
    path('eliminar_profcurso/<str:pk>/',views.Eliminar_ProfeCurs,name='eliminar_profcurso'),
    path('aula/<str:pk>/',views.ViewAulas_AlumnoAula,name='aula'),
    path('en_espera',views.ViewEn_Espera,name='en_espera'),
    path('asignar_alumno/<str:pk>/',views.Asignar_AlumnAula,name='asignar_alumno'),
    path('total_alumnos/',views.View_AlumnosTot,name='total_alumnos'),
    path('cursos/',views.ViewCursosAdmin,name='cursos'),
    path('agregar_curso/',views.AgregarCurso,name='agregar_curso'),
    path('editar_curso/<str:pk>/',views.EditarCurso,name='editar_curso'),
    path('eliminar_curso/<str:pk>/',views.EliminarCurso,name='eliminar_curso'),
    path('ver_PCursos/<str:pk>/',views.View_CursoProfesor,name='ver_PCursos'),
    path('ver_ACursos/<str:pk>/',views.View_CursoAlumno,name='ver_ACursos'),
    path('Alumno_porCurso/<str:pk>/<str:curso>/',views.ViewP_AlumnosporCurso,name="Alumno_porCurso"),
    path('verP_Notas/<str:pk>/<str:curso>/',views.ViewP_NotasAlumnos,name='verP_Notas'),
    path('agregar_nota/<str:pk>/',views.View_AgregarNotas,name='agregar_nota'),
    path('editar_nota/<str:pk>/',views.View_EditarNotas,name='editar_nota'),
    path('verA_Notas/<str:pk>/<str:cs>/',views.View_NotasAlumno,name='verA_Notas')
    
]