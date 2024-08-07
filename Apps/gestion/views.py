import json
from django.shortcuts import render, redirect
from django.views.generic.edit import ModelFormMixin
from .forms import AtletaForm,  CondicioFisicaForm
from .models import*
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from django.http import HttpResponse,JsonResponse
from django.db.models import Sum, Avg
from datetime import datetime, timedelta
from django.template.defaultfilters import floatformat

class login(TemplateView):
	template_name='inicio/login.html'

class home(TemplateView):
	template_name = 'index.html'

class RegistroPitcheo(View):
	model = Pitcheo 
	segundo_model = Atleta
	template_name = "Registro/registar_pitcheo.html"

	def get_queryset (self):
		return self.segundo_model.objects.all()

	def get_context_data(self, **kwargs):
		context = {}
		context['object'] = self.get_queryset()
		return context

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data())

	def post(self, request, *args, **kwargs):
		try:
			cantidad = float(request.POST.get('cantidad'))
			por_stick = request.POST.get('porcentaje_strick')
			por_bolas = request.POST.get('porcentaje_bolas')
			ponche = request.POST.get('ponche')
			recta = request.POST.get('rectas')
			curva = request.POST.get('curvas')
			cambio = request.POST.get('cambio')
			fecha = request.POST.get('fecha')
			nombre = request.POST.get('nombre')
			lista=[]
			lista = nombre.split(" ")
			nom = lista[0]
			apel = lista[1]
			query = self.segundo_model.objects.get(nombre = nom, apellido = apel)
			guardar = self.model.objects.create(cantida = cantidad,
				                                pro_strik = por_stick,
				                                pro_bola = por_bolas,
				                                pro_ponche = ponche,
				                                recta = recta,
				                                curva = curva,
				                                cambio = cambio,
				                                fecha = fecha,
				                                atleta = query)
			guardar.save()
			return redirect('Entrenamiento:listar')
		except Exception as e:
			return redirect('Entrenamiento:registro3')


class RegistroBateo(View):
	model = Bateo
	segundo_model = Atleta
	template_name = 'Registro/registro_bateo.html'

	def get_queryset (self):
		return self.segundo_model.objects.all()

	def get_context_data(self, **kwargs):
		context = {}
		context['object'] = self.get_queryset()
		return context

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data())

	def post(self, request, *args, **kwargs):
		try:
			lista=[]
			nombre = request.POST.get('nombre')
			lista = nombre.split(" ")
			nom = lista[0]
			apel = lista[1]
			fecha = request.POST.get('fecha')
			turnos = float(request.POST.get('turno'))
			hits = float(request.POST.get('hits'))
			average =  request.POST.get('average')
			ponche = float(request.POST.get('ponche'))
			query = self.segundo_model.objects.get(nombre = nom, apellido = apel )
			guardar = self.model.objects.create(turno = turnos,
				                                hits = hits,
				                                ponche_batiador = ponche,
				                                avg = average,
				                                fecha = fecha,
				                                atleta = query)
			guardar.save()
			return redirect('Entrenamiento:listar')
		except Exception as e:
			return redirect('Entrenamiento:registro4')
	   

class RegistroAtleta(CreateView):
	model = Atleta
	template_name = 'Registro/registro_atleta.html'
	form_class = AtletaForm
	success_url= reverse_lazy('Entrenamiento:listar')


class RegistroFisico(View):
	model = CondicioFisica
	segundo_model = Atleta
	template_name = 'Registro/registro_fisico.html'
	form_class =  CondicioFisicaForm
	
	def get_queryset (self):
		return self.segundo_model.objects.all()

	def get_context_data(self, **kwargs):
		context = {}
		context['form'] = self.form_class
		context['object'] = self.get_queryset()
		return context

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data())

	def post(self, request, *args, **kwargs ):
		try:
			form =self.form_class(request.POST)
			nombre = request.POST.get('nombre')
			lista=[]
			lista = nombre.split(" ")
			nom = lista[0]
			apel = lista[1]		
			edad = request.POST.get('edad')
			altura = request.POST.get('altura')
			objecto = self.segundo_model.objects.get(nombre = nom, apellido = apel )
			if not form.is_valid():
				formulario = form.cleaned_data
				guardar =self.model()
				guardar.peso = edad
				guardar.altura = altura
				guardar.tiempo_velocidad = formulario['tiempo_velocidad']
				guardar.atleta = objecto
				guardar.fecha = formulario['fecha']

				guardar.save()
				return redirect('Entrenamiento:listar')
			else:
				return render(request, self.template_name, {'form':form})
		except Exception as e:
			return redirect('Entrenamiento:registro2')




class Listar(ListView):
	template_name = 'listar_atleta.html'
	model = Atleta
	context_object_name ='Atletas'
	


class DetalleAtleta(DetailView):
	model = Atleta
	segundo_model = Bateo
	tercer_model = Pitcheo
	template_name ='Detalle/detalle.html'

	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		context['info'] = self.segundo_model.objects.filter(atleta_id=self.kwargs['pk'])
		context['info2'] = self.tercer_model.objects.filter(atleta_id=self.kwargs['pk'])
		return context


class ListarFisico(DeleteView):
	model = Atleta
	segundo_model = CondicioFisica
	template_name = 'listar_fisico.html'

	def get_context_data(self , **kwargs):
		context = super().get_context_data(**kwargs)
		context['info'] = self.segundo_model.objects.filter(atleta_id=self.kwargs['pk'])
		return context


class GraficaFisico(View):
	model = Atleta
	segundo_model = CondicioFisica
	template_name = 'Grafica/grafica_fisico.html'

	def promedio(self, dato):	
		promedios = []
		fecha_actual = datetime.now().date()
		for i  in range(1, 13):
			fecha_inicio_mes = fecha_actual.replace(month=i,day=1)
			fecha_fin_mes = fecha_inicio_mes.replace(day=1, month=i%12 +1 ) - timedelta(days=1)

			promedio = self.segundo_model.objects.filter(atleta_id=self.kwargs['pk'],
				                                         fecha__gte = fecha_inicio_mes,
				                                         fecha__lte = fecha_fin_mes).aggregate(promedios=Avg(dato))
			promedios.append(promedio['promedios'] or 0.0)
		return promedios	

	def get_context_data(self , **kwargs):
		context = {}
		context['peso'] = self.promedio("peso")
		context['altura'] = self.promedio("altura")
		context['tiempo_velocidad'] = self.promedio("tiempo_velocidad")
		return context

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data())


class GraficaBateo(View):
	model = Atleta
	segundo_model = Bateo
	template_name = 'Grafica/grafica_bateo.html'

	def promedio(self, dato):	
		promedios = []
		fecha_actual = datetime.now().date()
		for i  in range(1, 13):
			fecha_inicio_mes = fecha_actual.replace(month=i,day=1)
			fecha_fin_mes = fecha_inicio_mes.replace(day=1, month=i%12 +1 ) - timedelta(days=1)

			promedio = self.segundo_model.objects.filter(atleta_id=self.kwargs['pk'],
				                                         fecha__gte = fecha_inicio_mes,
				                                         fecha__lte = fecha_fin_mes).aggregate(promedios=Avg(dato))
			promedios.append(promedio['promedios'] or 0.0)
			#floatformat(promedios, 3)
		return promedios	

	def get_context_data(self , **kwargs):
		context = {}
		context['avg'] = self.promedio("avg")
		context['hits'] = self.promedio("hits")
		context['ponche_batiador'] = self.promedio("ponche_batiador")
		return context

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data())

class GraficaPitcheo(View):
	model = Atleta
	segundo_model = Pitcheo
	template_name = 'Grafica/grafica_pitcheo.html'

	def promedio(self, dato):	
		promedios = []
		fecha_actual = datetime.now().date()
		for i  in range(1, 13):
			fecha_inicio_mes = fecha_actual.replace(month=i,day=1)
			fecha_fin_mes = fecha_inicio_mes.replace(day=1, month=i%12 +1 ) - timedelta(days=1)

			promedio = self.segundo_model.objects.filter(atleta_id=self.kwargs['pk'],
				                                         fecha__gte = fecha_inicio_mes,
				                                         fecha__lte = fecha_fin_mes).aggregate(promedios=Avg(dato))
			promedios.append(promedio['promedios'] or 0.0)
			#floatformat(promedios, 3)
		return promedios

	def suma(self, dato2):	
		promedios = []
		fecha_actual = datetime.now().date()
		for i  in range(1, 13):
			fecha_inicio_mes = fecha_actual.replace(month=i,day=1)
			fecha_fin_mes = fecha_inicio_mes.replace(day=1, month=i%12 +1 ) - timedelta(days=1)

			promedio = self.segundo_model.objects.filter(atleta_id=self.kwargs['pk'],
					                                         fecha__gte = fecha_inicio_mes,
					                                         fecha__lte = fecha_fin_mes).aggregate(promedios=Sum(dato2))
			promedios.append(promedio['promedios'] or 0.0)
				
		return promedios	

	def get_context_data(self , **kwargs):
		context = {}
		context['ponche'] = self.promedio("pro_ponche")
		context['porcentaje_strick'] = self.promedio("pro_strik")
		context['porcentaje_bolas'] = self.promedio("pro_bola")

		context['recta'] = self.suma("recta")
		context['curva'] = self.suma("curva")
		context['Cambio'] = self.suma("cambio")
		return context

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, self.get_context_data())


class editar_actividad(UpdateView):
	model= Atleta
	form_class =  AtletaForm
	template_name="Modal/modal_editar_actividad.html"
	success_url = reverse_lazy('Entrenamiento:listar')
	

class eliminar_actividad (DeleteView):
	model = Atleta
	template_name="Modal/eliminar_actividad.html"
	success_url = reverse_lazy('Entrenamiento:listar')

class PruebaGrafica(View):
	template_name = "Grafica/prueba.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)



	







