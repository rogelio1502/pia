from django.db import models

# Create your models here.

class Estanteria(models.Model):

    modelo= models.CharField(verbose_name="Nombre del Modelo",max_length=50,null=False)
    color = models.CharField(verbose_name="Color",max_length=50,null=False)
    precio = models.FloatField(verbose_name="Precio",null=False)

    class Meta:
        verbose_name = "Estantenria"
        verbose_name_plural = "Estanterias"

    def __str__(self):
        return self.modelo

    
