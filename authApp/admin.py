from django.contrib import admin
from .models.user import User
from .models.account import Account

from .models.persona import Persona
from .models.empleado import Empleado
from .models.liquidacion_sueldo import Liquidacion_Sueldo
from .models.devengado import Devengado
from .models.horas import Horas
from .models.comision import Comision
from .models.deducidos import Deducidos
from .models.tipos_deducidos import Tipos_Deducidos
from .models.fsp import FSP
from .models.seguridad_social import Seguridad_Social
from .models.aportes_parafiscales import Aportes_Parafiscales
from .models.prestacion_social import Prestacion_Social

# Register your models here.


admin.site.register(Persona)
admin.site.register(Empleado)
admin.site.register(Liquidacion_Sueldo)
admin.site.register(Devengado)
admin.site.register(Horas)
admin.site.register(Comision)
admin.site.register(Deducidos)
admin.site.register(Tipos_Deducidos)
admin.site.register(FSP)
admin.site.register(Seguridad_Social)
admin.site.register(Aportes_Parafiscales)
admin.site.register(Prestacion_Social)
admin.site.register(User)
admin.site.register(Account)