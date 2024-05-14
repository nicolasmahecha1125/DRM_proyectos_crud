import json
from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from App.models import Empleado
from App.serializers import AdminSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from App.models import Empleado 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response


@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        
        if 'application/json' in request.content_type:
            try:
                data = json.loads(request.body)
                username = data.get('username')
                password = data.get('password')
                email = data.get('email')

               
                if not username or not password or not email:
                    return JsonResponse({'message': 'Faltan campos obligatorios'}, status=400)

                
                if User.objects.filter(username=username).exists():
                    return JsonResponse({'message': 'El usuario ya existe'}, status=402)

               
                user = User.objects.create_user(username=username, email=email, password=password)
                return JsonResponse({'message': 'Usuario creado con éxito', 'username': user.username}, status=201)
            except json.JSONDecodeError:
                return JsonResponse({'message': 'Error en el formato de datos JSON'}, status=400)
        else:
            return JsonResponse({'message': 'La solicitud no contiene datos JSON'}, status=400)

   
    return render(request, 'crear_user.html')
@csrf_exempt
def leer_empleados(request):
    
    if request.method == 'GET':
        empleados = Empleado.objects.all()  

   
    employee_data = []
    for empleado in empleados:
        employee_data.append({
            'id': empleado.id,
            'nombre': empleado.nombre,
            'apellido': empleado.apellido,
            'correo': empleado.email,
            'trabajos': empleado.trabajo  
        })

    
   
    return JsonResponse({'empleados': employee_data})
        
@csrf_exempt
def actualizar_empleado(request, id):
    empleado = Empleado.objects.get(pk=id)  
    if request.method == 'PUT':
        serializer = AdminSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)  
        else:
         return JsonResponse(serializer.errors, status=400)  
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
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
            


class EmpleadoList(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        empleados = Empleado.objects.all()
        serializer = AdminSerializer(empleados, many=True)
        return Response(serializer.data)

class EmpleadoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            empleado = Empleado.objects.get(pk=pk)
            serializer = AdminSerializer(empleado)
            return Response(serializer.data)
        except Empleado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            empleado = Empleado.objects.get(pk=pk)
            serializer = AdminSerializer(empleado, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Empleado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            empleado = Empleado.objects.get(pk=pk)
            empleado.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Empleado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)




