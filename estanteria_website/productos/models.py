from django.db import models

# Create your models here.

class Estanteria(models.Model):

    nombre_modelo= models.CharField(verbose_name="Nombre del Modelo",max_length=50,null=False)
    color = models.CharField(verbose_name="Color",max_length=50,null=False)
    precio = models.FloatField(verbose_name="Precio",null=False)
    piezas = models.IntegerField(verbose_name="Cantidad Piezas",null=False,default=0)

    class Meta:
        verbose_name = "Estantenria"
        verbose_name_plural = "Estanterias"

    def __str__(self):
        return self.nombre_modelo


class Locker(models.Model):

    nombre_modelo= models.CharField(verbose_name="Nombre del Modelo",max_length=50,null=False)
    color = models.CharField(verbose_name="Color",max_length=50,null=False)
    precio = models.FloatField(verbose_name="Precio",null=False)
    piezas = models.IntegerField(verbose_name="Cantidad Piezas",null=False,default=0)
    espacios = models.IntegerField(verbose_name="Cantidad Espacios",null=False,default=0)
   

    class Meta:
        verbose_name = "Locker"
        verbose_name_plural = "Lockers"

    def __str__(self):
        return self.nombre_modelo

class MueblesOficina(models.Model):

    nombre_modelo= models.CharField(verbose_name="Nombre del Mueble",max_length=50,null=False)
    color = models.CharField(verbose_name="Color",max_length=50,null=False)
    precio = models.FloatField(verbose_name="Precio",null=False)
    piezas = models.IntegerField(verbose_name="Cantidad Piezas",null=False,default=0)

    class Meta:
        verbose_name = "Mueble"
        verbose_name_plural = "Muebles"

    def __str__(self):
        return self.nombre_modelo


class CajaPlastica(models.Model):

    color = models.CharField(verbose_name="Color",max_length=50,null=False)
    altura = models.FloatField(verbose_name="Altura CM",null=False)
    base = models.FloatField(verbose_name="Base CM",null=False)
    fondo = models.FloatField(verbose_name="Fondo CM",null=False)
    precio = models.FloatField(verbose_name="Precio",null=False)
    piezas = models.IntegerField(verbose_name="Cantidad Piezas",null=False,default=0)



    class Meta:
        verbose_name = "Caja"
        verbose_name_plural = "Cajas"

    def __str__(self):
        return f"Caja {self.color} {self.altura} cm x {self.base} cm x {self.fondo} cm"

  

    
