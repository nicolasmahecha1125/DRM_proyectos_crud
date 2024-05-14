"""
URL configuration for DRM_proyectos_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_Empleado/', include('App.urls')),
    path('crear_usuario/', views.crear_usuario),
    path('leer_empleados/', views.leer_empleados),
    path('actualizar_empleado/<int:id>/', views.actualizar_empleado),
    path('empleados/', views.EmpleadoList.get),
    path('empleados/<int:pk>/', views.EmpleadoList.get),
    path('empleados/<int:pk>/update/', views.EmpleadoDetail.put),
    path('empleados/<int:pk>/delete/', views.EmpleadoDetail.delete)


]
