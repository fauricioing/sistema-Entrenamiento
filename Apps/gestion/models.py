from django.db import models



class Atleta(models.Model):
	cedula = models.CharField('apellido del jugador', max_length=100)
	nombre = models.CharField('nombre del jugador', max_length=100,)
	apellido = models.CharField('apellido del jugador', max_length=100)
	fecha_nacimiento = models.DateField('Fecha de nacimiento')
	direcion = models.CharField('apellido del jugador', max_length=100)
	imagen = models.ImageField(upload_to='imagenes/' )

	def __str__(self):
		return self.nombre + "  " + self.apellido

class Bateo(models.Model):
	turno = models.IntegerField()
	hits = models.IntegerField()
	ponche_batiador = models.IntegerField()
	avg = models.FloatField()
	fecha = models.DateField()
	atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE) 
	


class Pitcheo(models.Model):
	cantida =  models.IntegerField()
	pro_strik =  models.FloatField()
	pro_bola =  models.FloatField()
	pro_ponche =  models.IntegerField()
	recta = models.IntegerField()
	curva = models.IntegerField()
	cambio = models.IntegerField()
	fecha = models.DateField()
	atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE) 
	

class  CondicioFisica(models.Model):
	peso = models.FloatField('peso del jugador')
	altura = models.FloatField('altura del jugador')
	tiempo_velocidad = models.FloatField()
	atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
	fecha = models.DateField()

	


