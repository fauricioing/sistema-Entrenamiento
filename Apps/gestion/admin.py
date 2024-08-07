"""el archivo admin  contiene funciones y clases del modulo
	admin  es decir el archivo facilita el uso d todas la heramienta 
	que tiene dicha clases como tambien el registro de los modelos, 
	lecturas, modificacion y elimanacion...
"""
from django.contrib import admin
from .models import*

admin.site.site_header= "Inicio de Seccion"
admin.site.site_title= " Gestional  los atletas"
admin.site.index_title ="Administrador"
"""
	adimin.site.site_atributo =  etributo hace referencia a la
	interfaz, es decir se puede cambiar muchos atributos como
	el titulo, contenido, eh imagenes
"""
admin.site.register(Atleta)
admin.site.register(CondicioFisica)
admin.site.register(Bateo)
admin.site.register(Pitcheo)
"""
	Admin.site.registro(Modelo) = esta funcion hace referencia a los
	modelo es decir se utiliza para registrar los modelo en o la interfa
	del Admin
"""




