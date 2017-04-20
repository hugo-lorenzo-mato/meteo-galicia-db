from django.shortcuts import render
import urllib3
import json
import requests

# Create your views here.

def formulario(request):
    return render(request,'consulta/formulario/form.html', None)


def resultado(request):

    # Consultamos el lugar al usuario
    lugar = 'vilalba'
    # Preparamos los datos de la petición
    api_code = 'tcZwyEj10Lb5W11usQMSM52QIlCutCCI64LfHv8AeuJsp9aE1F16tsn4yvdK0R52'
    parametros = {'location': lugar, 'API_KEY': api_code}
    url = 'http://servizos.meteogalicia.es/apiv3/findPlaces'

    # Enviamos la peticion
    peticion = requests.get(url, parametros)

    # Obtenemos la respuesta
    respuesta = json.loads(peticion.text)

    # Obtenemos nuestras coordenadas
    longitud = str(respuesta['features'][0]['geometry']['coordinates'][0])
    latitud = str(respuesta['features'][0]['geometry']['coordinates'][1])




    # Preparamos los datos de la petición
    url = 'http://servizos.meteogalicia.es/apiv3/getNumericForecastInfo'
    coordenadas = longitud + ',' + latitud
    parametros2 = {'coords': coordenadas, 'API_KEY': api_code}
    # Enviamos la peticion
    peticion2 = requests.get(url, parametros2)

    # Obtenemos la respuesta

    respuesta2 = json.loads(peticion2.text)



    # Si queremos obtener unos datos concretos, le pasamos como parámetros las variables que deseamos
    variables = 'temperature'  # 'sky_state,temperature,precipitation_amount,wind'
    parametros3 = {'coords': coordenadas, 'variables': variables, 'API_KEY': api_code}
    # Enviamos la peticion
    peticion3 = requests.get(url, parametros3)
    # Obtenemos la respuesta
    respuesta3 = json.loads(peticion3.text)



    return render(request, 'consulta/resultado/imprimir.html', {'respuesta3': respuesta3})