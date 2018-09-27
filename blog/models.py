from django.db import models
from django.utils import timezone
# Create your models here.

class Habitacion(models.Model):
	Codigo_hab = models.CharField(max_length = 7)
	Numero_hab = models.CharField(max_length=15)
	Precio = models.DecimalField(max_digits=10,decimal_places=2)


	def __str__(self):
		return self.Numero_hab

class Cliente(models.Model):
	Nombre_cl = models.CharField(max_length = 25)
	Apellido_cl = models.CharField(max_length = 25)
	Direccion_cl = models.CharField(max_length = 20)
	Telefono_cl = models.CharField(max_length = 25)
	Nit_cl = models.CharField(max_length = 11)


	def __str__(self):
		return self.Nit_cl

class Productos(models.Model):
	Nombre = models.CharField(max_length=25)
	Descripcion = models.CharField(max_length=25)
	Costo = models.DecimalField(max_digits=10, decimal_places=2)
	Cantidad = models.CharField(max_length=25)
	Estado = models.BooleanField()

	def __str__(self):
		return self.Nombre

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title= models.CharField(max_length=200)
	text = models.TextField()
	Create_date = models.DateTimeField(
 			default= timezone.now)
	published_date = models.DateTimeField(
    		blank=True, null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
