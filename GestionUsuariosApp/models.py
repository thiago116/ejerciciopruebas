from django.db import models

# Create your models here.

class Ambiente(models.Model):
    codigo_ambiente=models.IntegerField(unique=True, blank=True, null=True)
    nombre_ambiente=models.CharField(max_length=30)
    ubicacion=models.CharField(max_length=30)


class Subambiente(models.Model):
    codigo_subambiente= models.ForeignKey(Ambiente,on_delete=models.CASCADE)
    nombre_subambiente= models.CharField(max_length=30,blank=False,null=True)
    ubicacion_subambiente= models.CharField(max_length=30,blank=False,null=True)



