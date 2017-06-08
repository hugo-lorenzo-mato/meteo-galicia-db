from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.formulario, name='formulario'),
    url(r'^grafico/simple.png$', views.simple, name='simple'),
    url(r'^grafico/rosavientos.png$', views.rosaVientos, name='rosaVientos'),
]