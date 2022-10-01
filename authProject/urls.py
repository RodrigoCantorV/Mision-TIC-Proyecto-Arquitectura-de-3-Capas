from django.contrib import admin
from django.urls import path
from authApp.views.user.userCreateiIew import UserCreateView
from authApp.views.user.userDetailView import UserDetailView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from authApp.views.vistas_usuarios.login import inicio_sesion

## CRUD DE Persona
#CRUD FORMA 1
from authApp.views.vistas_personas.personaCreateView import PersonaCreateView
from authApp.views.vistas_personas.personaReadView import PersonaReadView
from authApp.views.vistas_personas.personaReadOneView import PersonaReadOneView
from authApp.views.vistas_personas.personaUpdateView import PersonaUpdateView
from authApp.views.vistas_personas.personaDeleteView import PersonaDeleteView

#CRUD FORMA 2
from authApp.views.vistas_personas_Forma_2.personaCreateView import add_items
from authApp.views.vistas_personas_Forma_2.personaReadView import view_items
from authApp.views.vistas_personas_Forma_2.personaReadOneView import view_items_one
from authApp.views.vistas_personas_Forma_2.personaUpdateView import update_items
from authApp.views.vistas_personas_Forma_2.personaDeleteView import delete_items

# GET Y POST FORMA 3
from django.urls import include
from rest_framework.routers import DefaultRouter
from authApp.views.vistas_personas_Forma_3.personaViewSet import PersonaViewSet
router = DefaultRouter()
router.register(r'',PersonaViewSet)
    # NOTA IMPORTANTE: 
    # PARA ESTA TERCERA FORMA DEBEMOS DEJAR DE ULTIMAS LOS COMANDOA MAKEMIGRATIONS Y MIGRATE

#from authApp.views.vistas_empleados.empleadosHttpResponse  import registrar_empleado
#from authApp.views.vistas_empleados.empleadosHttpResponse  import eliminar_empleado
#from authApp.views.vistas_empleados.empleadosHttpResponse  import modificar_empleado

from authApp.views.vistas_empleados.empleadoViewSet import EmpleadoViewSet


urlpatterns = [
    path('', inicio_sesion),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('usuario/crear',UserCreateView.as_view()),
    path('usuario/<int:pk>/',UserDetailView.as_view()),

## CRUD DE Persona
    #FORMA 1
    path('persona/crear/',PersonaCreateView.as_view()),
    path('persona/listar/',PersonaReadView.as_view()),
    path('persona/listar/<int:pk>/',PersonaReadOneView.as_view()),
    path('persona/actualizar/<int:pk>/',PersonaUpdateView.as_view()),
    path('persona/eliminar/<int:pk>/',PersonaDeleteView.as_view()),

    #FORMA 2
    path('persona2/crear/',add_items),
    path('persona2/listar/', view_items),
    path('persona2/listar/<int:pk>/', view_items_one),
    path('persona2/actualizar/<int:pk>/', update_items),
    path('persona2/eliminar/<int:pk>/',delete_items),

    #FORMA 3
    path('persona3/',include(router.urls)),
   
    path('empleado/listar/', EmpleadoViewSet.as_view({'get':'list'})),
   
   # path('registrarEmpleado/', registrar_empleado),
   # path('eliminarEmpleado/', eliminar_empleado),
   # path('modificarEmpleado/', modificar_empleado),
]
