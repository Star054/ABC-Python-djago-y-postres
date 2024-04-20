from django.urls import path, include
from . import views
from .views import list_alumnos, create_alumnos, delete_alumno, edit_alumno, lista_alumnos

urlpatterns = [
    path('', list_alumnos),  
    path('lista_alumnos/', lista_alumnos, name='lista_alumnos'),
    path('list_alumnos/', list_alumnos, name='list_alumnos'),
    path('new/', create_alumnos),
    path('delete/<int:alumno_id>/', delete_alumno, name='delete_alumno'),
    path('edit/<int:alumno_id>/', edit_alumno, name='edit_alumno'),
    path('api/', views.alumnos_list),

]


