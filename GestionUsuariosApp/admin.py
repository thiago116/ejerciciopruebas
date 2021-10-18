from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib import admin
from GestionUsuariosApp.models import Ambiente,Subambiente

# Register your models here.


class AmbienteAdmin(admin.ModelAdmin):
    list_display=("codigo_ambiente","nombre_ambiente","ubicacion")
    

admin.site.register(Ambiente, AmbienteAdmin)
admin.site.register(Subambiente)
