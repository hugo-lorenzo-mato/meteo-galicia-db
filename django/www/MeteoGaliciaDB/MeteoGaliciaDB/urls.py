"""MeteoGaliciaDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'', include('portada.urls', namespace='portada', app_name='portada')),
    url(r'^consulta/', include('consulta.urls', namespace='consulta', app_name='consulta')),
    url(r'^contacto/', include('contacto.urls', namespace='contacto', app_name='contacto')),
    url(r'^faq/', include('faq.urls', namespace='faq', app_name='faq')),
    url(r'^registro/', include('registros.urls', namespace='registros', app_name='registros')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <-- para entrar con face y twitter

]


'''
LOGIN_REDIRECT_URL = '/'


SOCIAL_AUTH_FACEBOOK_KEY = '394095107651835'
SOCIAL_AUTH_FACEBOOK_SECRET = '4c2b5bdd6a4b8b25acc7c109c613b108'
'''