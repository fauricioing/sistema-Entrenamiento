
from django.contrib import admin
from django.conf import  settings
from django.conf.urls.static import static
from django.urls import path, include
from Apps.Usuarios.views import Login, logoutUsuario
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Entrenamiento/', include(('Apps.gestion.urls', 'Entrenamiento'))),
    path('accounts/login/',Login.as_view(), name = 'login'),
    path('logout/',login_required(logoutUsuario),name = 'logout')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
