from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/', views.alumnos_list, name='alumnos_list'),
    path('alumnos/<int:pk>/', views.alumno_detail, name='alumno_detail'),
]
