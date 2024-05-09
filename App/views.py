import json
from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from App.models import Empleado
from App.serializers import EmpleadoSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test

@csrf_exempt
def crear_empleado(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data['nombre']
        apellido = data['apellido']
        email = data['email']
        departamento = data['departamento']
        salario = data['salario']

        empleado = Empleado.objects.create(
            nombre = nombre,
            apellido = apellido,
            email = email,
            departamento = departamento,
            salario = salario
        )

        response_data = {
            'message': 'Empleado creado con éxito',
            'data': {
                'id': empleado.id, 
                'nombre': empleado.nombre,
                'apellido': empleado.apellido,
                'email': empleado.email,
                'departamento': empleado.departamento,
                'salario': empleado.salario,
                }
            }
        return JsonResponse(response_data,status=201)
    return JsonResponse({'message':'Metodo no permitido'}, status=405)    

@csrf_exempt
def leer_empleados(request):
    if request.method == 'GET':
        empleados = Empleado.objects.all()
        serialized_data = EmpleadoSerializer(empleados, many=True)
        return JsonResponse(serialized_data.data, status=status.HTTP_200_OK)
    return JsonResponse({'message':'Metodo no permitido'}, status=status.HTTP_405)

@csrf_exempt
def actualizar_empleado(request, id):
    try:
        empleado = Empleado.objects.get(pk=id)
    except Empleado.DoesNotExist:
        return JsonResponse({'message': 'Empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = EmpleadoSerializer(empleado,data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    return JsonResponse({'message': 'Metodo no permitido'}, status=status.HTTP_405)

@csrf_exempt
def eliminar_empleado(request,id):
    try:
        empleado = Empleado.objects.get(pk=id)
    except Empleado.DoesNotExist:
        return JsonResponse({'message':'Empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        empleado.delete()
        return JsonResponse({'message': 'Empleado eliminado'}, status=status.HTTP_204_NO_CONTENT)
    return JsonResponse({'message': 'Metodo no permitido'}, status=status.HTTP_405)
    
@csrf_exempt        
def login_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return JsonResponse({'message': 'Usuario auteticado'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'message':'Usuario no activo'}, status=status.HTTP_401_UNAUTHORIZED)
        return JsonResponse({'message': 'Metodo no permitido'}, status=status.HTTP_405)
            





    





