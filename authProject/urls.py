"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from authApp.vistas_usuarios.login import inicio_sesion
from authApp.views.vistas_empleados.registrar_empleado import registrar_empleado
from authApp.views.vistas_empleados.eliminar_empleado import eliminar_empleado
from authApp.views.vistas_empleados.modificar_empleado import modificar_empleado
from authApp.views.vistas_nomina.listar_nomina import listar_nomina
urlpatterns = [
     path('', inicio_sesion),
    path('admin/', admin.site.urls),
    path('registrarEmpleado/', registrar_empleado),
    path('eliminarEmpleado/', eliminar_empleado),
    path('modificarEmpleado/', modificar_empleado),
    path('listarNomina/', listar_nomina)
]
