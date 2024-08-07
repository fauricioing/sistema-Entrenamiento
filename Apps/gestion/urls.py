from django.urls import  path
from .views import *
from django.conf import  settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns =[
	path('home/',login_required(home.as_view()), name = 'index'),
	path('login/', login.as_view(), name = 'login'),

	path ('registro/',login_required(RegistroAtleta.as_view()), name = 'registro'),
	path('registro2/', login_required(RegistroFisico.as_view()), name = 'registro2'),
	path('registro3/', login_required(RegistroPitcheo.as_view()), name = 'registro3'),
	path('registro4/', login_required(RegistroBateo.as_view()), name = 'registro4'),
	path('listar/', login_required(Listar.as_view()), name = 'listar'),
	path('listar_fisico/<int:pk>/', login_required(ListarFisico.as_view()), name = 'listar_fisico'),
	path("detalle_atleta/<int:pk>/" , login_required(DetalleAtleta.as_view()) , name= "detalle_atleta"),
	path("editar_actividad/<int:pk>/", editar_actividad.as_view(), name= "editar_actividads"),
    path("eliminar_actividad/<int:pk>/" , eliminar_actividad.as_view() , name="eliminar_actividad"),

    path("prueba/", login_required(PruebaGrafica.as_view()), name = 'prueba'),
    path('grafica_fisico/<int:pk>/', login_required(GraficaFisico.as_view()), name = 'grafica_fisico'),
    path('grafica_bateo/<int:pk>/', login_required(GraficaBateo.as_view()), name = 'grafica_bateo'),
     path('grafica_pitcheo/<int:pk>/',login_required(GraficaPitcheo.as_view()), name = 'grafica_pitcheo')



	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)