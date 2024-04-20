from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Alumno
from .forms import AlumnoForm
from .serializers import AlumnoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})



# Vista para listar todos los alumnos (API)
@api_view(['GET', 'POST'])
def alumnos_list(request):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para obtener, actualizar o eliminar un alumno específico (API)
@api_view(['GET', 'PUT', 'DELETE'])
def alumno_detail(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'GET':
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    