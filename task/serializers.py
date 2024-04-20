from rest_framework import serializers
from .models import Alumno, Pago

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['carnet', 'nombres', 'apellidos', 'correo_electronico', 'fecha_nacimiento']

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['alumno', 'numero_boleta', 'codigo_banco', 'fecha_pago']

class AlumnoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class AlumnoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['nombres', 'apellidos', 'correo_electronico', 'fecha_nacimiento']

class PagoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class PagoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['numero_boleta', 'codigo_banco', 'fecha_pago']
