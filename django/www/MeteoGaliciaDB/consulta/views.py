import datetime
from django.shortcuts import render
import urllib3
import json
import requests
from . import forms
from datetime import timedelta
from django.contrib.auth.decorators import login_required


@login_required(login_url='/registro/acceso')
def formulario(request):
    form = forms.FormRequest()
    if request.method == 'POST':
        form = forms.FormRequest(request.POST)
        if form.is_valid():
            lugar = form.cleaned_data['Lugar']
            horas = form.cleaned_data['Prediccion']
            variables_posibles = form.cleaned_data['Variables']
            variables = ",".join(str(x) for x in variables_posibles)
            #if 'temperature' in variables_posibles:
            #    variables = "" + temperature
            # Consultamos el lugar al usuario
            # Preparamos los datos de la petición
            api_code = 'tcZwyEj10Lb5W11usQMSM52QIlCutCCI64LfHv8AeuJsp9aE1F16tsn4yvdK0R52'
            '''
            key = open('meteosix_api_key', 'r')
            clave = ""
            for lineas in key:
                clave = clave + lineas
            '''
            parametros = {'location': lugar, 'API_KEY': api_code, 'format': 'application/json'}
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
            hora_actual = datetime.datetime.now().isoformat()
            hora_actual = hora_actual[:-7]
            hora_siguiente = (datetime.datetime.now() + timedelta(hours=int(horas))).isoformat()
            hora_siguiente = hora_siguiente[:-7]

            # Si queremos obtener unos datos concretos, le pasamos como parámetros las variables que deseamos
            parametros3 = {'coords': coordenadas, 'variables': variables, 'API_KEY': api_code,
                           'format':'text/html', 'endTime':hora_siguiente, 'lang':"es"}
            # Enviamos la peticion
            peticion3 = requests.get(url, parametros3)
            # Obtenemos la respuesta
            #respuesta3 = json.loads(peticion3.text)
            return render(request, 'consulta/resultado/imprimir.html', {'variables': variables,
                                                                        'respuesta3': peticion3.content,
                                                                        'lugar': lugar,
                                                                        'hora_actual': hora_actual,
                                                                        'hora_siguiente': hora_siguiente,
                                                                        'dias': horas,
                                                                        'Variables': variables_posibles,
                                                                        'latitud':latitud,
                                                                        'longitud': longitud})

    return render(request,'consulta/formulario/form.html', {'form':form})












'''
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
'''
