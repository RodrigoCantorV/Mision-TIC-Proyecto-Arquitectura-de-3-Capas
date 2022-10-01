from django.http import HttpResponse
# Create your views here.

def eliminar_empleado(request):
 return HttpResponse("Modulo de eliminacion de empleados")
 
def modificar_empleado(request):
 return HttpResponse("Modulo de modificacion de empleados")
 
def registrar_empleado(request):
 return HttpResponse("Modulo de registro de usuario")
 
