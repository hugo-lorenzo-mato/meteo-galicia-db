from django.conf.urls import url
from . import views

urlpatterns = [
    #127.0.0.0:8000/ o nuestro dominio principal
    url(r'^$', views.index, name="index"),
]