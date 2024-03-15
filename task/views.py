from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .forms import AlumnoForm


def list_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'list_alumnos.html', {"alumnos": alumnos})

def create_alumnos(request):
    if request.method == 'POST':
        carnet = request.POST.get('carnet')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        correo_electronico = request.POST.get('correoElectronico')
        fecha_nacimiento = request.POST.get('fechaNacimiento')

        # Crear el objeto Alumno con los valores proporcionados
        alumno = Alumno.objects.create(
            carnet=carnet,
            nombres=nombres,
            apellidos=apellidos,
            correo_electronico=correo_electronico,
            fecha_nacimiento=fecha_nacimiento
        )
        return redirect('/task/')
    else:
        return redirect('list_alumnos')  # Redirigir a la vista list_alumnos
    

    

def delete_alumno(request, alumno_id):
    alumno = Alumno.objects.get(pk=alumno_id)
    alumno.delete()
    return redirect('list_alumnos')

def edit_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, pk=alumno_id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('list_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
        return render(request, 'edit_alumno.html', {'form': form, 'alumno': alumno})
