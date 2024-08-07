"""
El archivo Forms Contiene la Clases Forms;   los Objectos Forms
son todo aquello que esta Relacionado con el formulario de lo 
templates (intrefaz:html);  pero esta clase es interna de django,
esta ya estructurada para diferentes casos; tambien afreces  metodo
sde validacion de formulario,  estilo de formulario ect........
"""
import re
from django import forms
from .models import *
from django.core.exceptions import ValidationError


class CondicioFisicaForm(forms.ModelForm):
	class Meta:
		"""
		 class Meta: define el  Atributo model(modelo) a utilizar;
		 fields : es  un arreglo con cada atributos del modelo que se esta
		 utilizado;
		 labels :  es un disionario con cojunto de datos dicho datos se va
		 a mostrar en  templates(html) como etiquetas <label>;
		 widgets : es un dicionarios de Datos; contiene los
		 atributos del modelo pero se encarga de darle estilo de boostrap en el
		 template (html)
		"""
		model = CondicioFisica
		fields = ['peso', 'altura', 'tiempo_velocidad', 'atleta', 'fecha']
		labels = {
		'peso': 'peso',
		'altura':'Altura',
		'tiempo_velocidad':'Tiempo de Velocidad',
		'atleta':'Atleta',
		'fecha': 'fecha' 
		}
		widgets = {
			'peso':forms.NumberInput(attrs={'class':'form-control'}),
			'altura':forms.NumberInput(attrs={'class':'form-control'}),
			'tiempo_velocidad': forms.NumberInput(attrs={'class':'form-control'}),
			#'atleta': forms.Select(attrs={'class':'form-control'}),
			'fecha':forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
		}


class AtletaForm(forms.ModelForm):

	class Meta:
		model = Atleta
		fields = ['imagen','cedula','nombre','apellido','fecha_nacimiento','direcion']
		labels = {
		'imagen': 'Foto de Perfil: ',
		'cedula': 'cedula',
		'nombre':'Nombre del jugador',
		'apellido':'Apellido del Jugador',
		'fecha_nacimiento':'Fecha de Nacimiento',
		'direcion': 'Direcion' 
		}

		widgets = {
			'cedula':forms.TextInput(attrs={'class':'form-control'}),
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellido':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento':forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
			'direcion':forms.TextInput(attrs={'class':'form-control'}),

		}


	def clean_cedula(self):
			#patron = re.compile("^\w+$")
			cedula = self.cleaned_data.get('cedula')
			if not re.match(r'\d+$', cedula) or len(cedula)>8:
				raise forms.ValidationError("Error! solo debe ser numero y un maximo de 8 caracteres")
			else:
				
				if Atleta.objects.filter(cedula =cedula).exists():
					raise forms.ValidationError("Error! la cedula ya se encuentra en uso")	
			return cedula	

	def clean_nombre(self):
		nombre = self.cleaned_data.get('nombre')
		if not re.match(r'[a-zA-Z\s]+$', nombre) or nombre == "":
			raise forms.ValidationError("debe ser solo letras y  es un campo obligatorio")
		return nombre

	def clean_apellido(self):
		apellido = self.cleaned_data.get('apellido')
		if not re.match(r'[a-zA-Z\s]+$', apellido) or apellido == "":
			raise forms.ValidationError("debe ser solo letras y  es un campo obligatorio")
		return apellido





