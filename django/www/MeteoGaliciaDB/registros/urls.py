from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^formulario/', views.registro, name='registro'),
    url(r'^acceso/', views.user_login, name='user_login'),
    url(r'^salir/$', views.user_logout, name='salir'),

 ]