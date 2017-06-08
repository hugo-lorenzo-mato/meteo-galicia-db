from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import json
import requests
from . import forms
from datetime import timedelta
from django.contrib.auth.decorators import login_required

#Para imprimir el plot
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import io
from io import *


import math
## De librerías de terceros
import numpy as np
import matplotlib.pyplot as plt

# bokeh

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.models import Range1d
from bokeh.charts import color, marker



import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter


from django.shortcuts import render
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import io
from io import *


@login_required(login_url='/registro/acceso')
def formulario(request):
    form = forms.FormRequest()
    if request.method == 'POST':
        form = forms.FormRequest(request.POST)
        if form.is_valid():
            lugar = form.cleaned_data['Lugar']
            horas = form.cleaned_data['Prediccion']
            variables_posibles = form.cleaned_data['Variables']
            grafica = form.cleaned_data['Grafica']
            variables = ",".join(str(x) for x in variables_posibles)
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
            return render(request, 'consulta/resultado/imprimir.html', {'variables': variables,
                                                                        'respuesta3': peticion3.content,
                                                                        'lugar': lugar,
                                                                        'hora_actual': hora_actual,
                                                                        'hora_siguiente': hora_siguiente,
                                                                        'dias': horas,
                                                                        'Variables': variables_posibles,
                                                                        'latitud':latitud,
                                                                        'longitud': longitud,
                                                                        'grafica':grafica})

    return render(request,'consulta/formulario/form.html', {'form': form})



'''
Lo estoy llamando desde el método formulario de arriba
'''
def simple(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig = Figure()
    ax = fig.add_subplot(111)
    x = []
    y = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now += delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response



def rosaVientos(request):
    import random
    import django
    import datetime
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    ## De la librería estándar
    import math
    ## De librerías de terceros
    import numpy as np
    import matplotlib.pyplot as plt

    fig = Figure()

    ## Creamos un conjunto de 1000 datos entre 0 y 1 de forma aleatoria
    ## a partir de una distribución estándar normal
    datos = np.random.randn(1000)
    ## Discretizamos el conjunto de valores en n intervalos,
    ## en este caso 8 intervalos
    datosbin = np.histogram(datos, bins=np.linspace(np.min(datos), np.max(datos), 9))[0]
    ## Los datos los queremos en tanto por ciento
    datosbin = datosbin * 100. / len(datos)
    ## Los datos los queremos en n direcciones/secciones/sectores,
    ## en este caso usamos 8 sectores de una circunferencia
    sect = np.array([90, 45, 0, 315, 270, 225, 180, 135]) * 2. * math.pi / 360.
    nombresect = ['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE']
    ## Dibujamos la rosa de frecuencias
    plt.axes([0.1, 0.1, 0.8, 0.8], polar=True)
    plt.bar(sect, datosbin, align='center', width=45 * 2 * math.pi / 360.,
            facecolor='b', edgecolor='k', linewidth=2, alpha=0.5)
    plt.thetagrids(np.arange(0, 360, 45), nombresect, frac=1.1, fontsize=10)
    plt.title(u'Procedencia de las nubes en marzo')
    #plt.show()

    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response






'''


##################################################################################

   Dejo esto por aquí por si bokeh porque arriba voy a probar con otro método

##################################################################################



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
            # Preparamos los datos de la petición
            api_code = 'tcZwyEj10Lb5W11usQMSM52QIlCutCCI64LfHv8AeuJsp9aE1F16tsn4yvdK0R52'
            ''''''
            key = open('meteosix_api_key', 'r')
            clave = ""
            for lineas in key:
                clave = clave + lineas
            ''''''
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

            # Just an example

            datos = np.random.randn(1000)
            ## Discretizamos el conjunto de valores en n intervalos,
            ## en este caso 8 intervalos
            datosbin = np.histogram(datos,
                                    bins=np.linspace(np.min(datos), np.max(datos), 9))[0]
            ## Los datos los queremos en tanto por ciento
            datosbin = datosbin * 100. / len(datos)
            ## Los datos los queremos en n direcciones/secciones/sectores,
            ## en este caso usamos 8 sectores de una circunferencia
            sect = np.array([90, 45, 0, 315, 270, 225, 180, 135]) * 2. * math.pi / 360.
            nombresect = ['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE']
            ## Dibujamos la rosa de frecuencias
            plt.axes([0.1, 0.1, 0.8, 0.8], polar=True)
            plt.bar(sect, datosbin, align='center', width=45 * 2 * math.pi / 360.,
                    facecolor='b', edgecolor='k', linewidth=2, alpha=0.5)
            plt.thetagrids(np.arange(0, 360, 45), nombresect, frac=1.1, fontsize=10)
            plt.title(u'Procedencia de las nubes en marzo')
            #plt.show()
            #plot = figure()
            #plot.circle([1, 2], [3, 4])
            script, div = components(plt, CDN)
            return render(request, 'consulta/resultado/imprimir.html', {'variables': variables,
                                                                        'respuesta3': peticion3.content,
                                                                        'lugar': lugar,
                                                                        'hora_actual': hora_actual,
                                                                        'hora_siguiente': hora_siguiente,
                                                                        'dias': horas,
                                                                        'Variables': variables_posibles,
                                                                        'latitud':latitud,
                                                                        'longitud': longitud,
                                                                        "the_script": script,
                                                                        "the_div": div})

    return render(request,'consulta/formulario/form.html', {'form': form})


'''