from django.urls import path
from .views import list_alumnos, create_alumnos, delete_alumno, edit_alumno

urlpatterns = [
    path('', list_alumnos),  # Esta es la ruta raíz
    path('list_alumnos/', list_alumnos, name='list_alumnos'),
    path('new/', create_alumnos),
    # Otras rutas aquí si es necesario
    path('delete/<int:alumno_id>/', delete_alumno, name='delete_alumno'),
    path('edit/<int:alumno_id>/', edit_alumno, name='edit_alumno'),

]

