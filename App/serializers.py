from rest_framework import serializers
from App.models import Empleado

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'