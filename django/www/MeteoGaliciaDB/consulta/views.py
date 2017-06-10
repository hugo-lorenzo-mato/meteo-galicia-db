from django.shortcuts import render
import json
import requests
from . import forms
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from pylab import *
from pandas import DataFrame
import string
import random


key_meteosix = 'tcZwyEj10Lb5W11usQMSM52QIlCutCCI64LfHv8AeuJsp9aE1F16tsn4yvdK0R52'

key_aemet = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaWd1ZWxvdXZpbmhhQGdtYWlsLmNvbSIsImp0aSI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsImV4cCI6MTQ5OTE2MjExNiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE0OTEzODYxMTYsInVzZXJJZCI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsInJvbGUiOiIifQ.w0OazTbsiZdI5YQXCMIRnny_f0TwWF7leFvik1WeA8s"




def generador_nombre(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@login_required(login_url='/registro/acceso')
def formulario(request):
    form = forms.FormRequest()
    if request.method == 'POST':
        form = forms.FormRequest(request.POST)
        if form.is_valid():
            '''
            ##########################################################
            Recuperamos los datos del formulario
            ##########################################################
            '''
            lugar = form.cleaned_data['Lugar']
            horas = form.cleaned_data['Prediccion']
            longitud = form.cleaned_data['Longitud']
            latitud = form.cleaned_data['Latitud']
            variables_posibles = form.cleaned_data['Variables']
            tipoGrafica = form.cleaned_data['Grafica']
            variables = ",".join(str(x) for x in variables_posibles)
            año = form.cleaned_data['Año']
            estacion = form.cleaned_data['Estacion_meteorológica']
            if ((lugar) or (longitud and latitud)):
                pass
            else:
                aviso = "¡¡¡Debe cubrir latitud y longitud o, de no hacerlo, indicar un lugar válido!!!"
                return render(request, 'consulta/formulario/form.html', {'form': form, 'aviso': aviso})
            '''
            ##########################################################
            Preparamos los datos para meteosix
            ##########################################################
            '''
            if (longitud and latitud):
                api_code = key_meteosix
                pass
            else:
                api_code = key_meteosix
                parametros = {'location': lugar, 'API_KEY': api_code, 'format': 'application/json'}
                url = 'http://servizos.meteogalicia.es/apiv3/findPlaces'
                peticion = requests.get(url, parametros)
                respuesta = json.loads(peticion.text)
                longitud = str(respuesta['features'][0]['geometry']['coordinates'][0])
                latitud = str(respuesta['features'][0]['geometry']['coordinates'][1])
            '''
            ##########################################################
            Una vez que tenemos las coordenadas obtenemos los datos
            ##########################################################
            '''
            url = 'http://servizos.meteogalicia.es/apiv3/getNumericForecastInfo'
            coordenadas = longitud + ',' + latitud
            hora_actual = datetime.datetime.now().isoformat()
            hora_actual = hora_actual[:-7]
            hora_siguiente = (datetime.datetime.now() + timedelta(hours=int(horas))).isoformat()
            hora_siguiente = hora_siguiente[:-7]
            parametros3 = {'coords': coordenadas, 'variables': variables, 'API_KEY': api_code,
                           'format': 'text/html', 'endTime': hora_siguiente, 'lang': "es"}
            peticion3 = requests.get(url, parametros3)
            '''
            ##########################################################
            Preparamos los datos para AEMET
            ##########################################################
            '''
            querystring = {"api_key": key_aemet}
            url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/mensualesanuales/datos/anioini/" \
                  + año + "/aniofin/" + año + "/estacion/" + estacion
            response = requests.request("GET", url, params=querystring, verify=False)
            cont = json.loads(response.text)
            cont = cont['datos']
            response = requests.request("GET", cont, verify = False)
            datos = json.loads(response.text)
            '''
            ##########################################################
            Análisis de datos con Pandas
            ##########################################################
            '''
            # Indices de los DataFrames
            temperaturas = [ 'tm_mes', 'ta_max', 'ta_min', 'fecha', 'indicativo']
            precipitacions = ['p_mes']
            vento = ['w_med', 'w_racha']
            humedad = ['hr']
            indice = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                      'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'Resumen']

            '''
            ##########################################################
            Gráficas
            ##########################################################
            '''
            nombre_png = generador_nombre()
            if ( tipoGrafica == "histogramaTemperaturas"):
                '''
                TEMPERATURAS
                '''
                # Creamos el DataFrame
                frame_tem = DataFrame(datos, columns = temperaturas, index = indice)
                # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
                frame_tem = frame_tem.iloc[0:12]
                # Borramos valores nulos
                frame_tem = frame_tem.dropna()
                #Procedemos a limpiar las filas del DataFrame
                temperatura_max = frame_tem.ta_max.map(lambda x: x.replace('(', ',')).map(lambda x: x.split(',')). \
                    map(lambda x: x[0]).map(lambda x: float(x))
                temperatura_min = frame_tem.ta_min.map(lambda x: x.replace('(', ',')).map(lambda x: x.split(',')). \
                    map(lambda x: x[0]).map(lambda x: float(x))
                temperatura_media = frame_tem.tm_mes
                temperatura_fechas = frame_tem.fecha.map(lambda x: x.replace('-', ',')).map(lambda x: x.split(',')). \
                    map(lambda x: x[1])

                data = { 'Temperatura Maxima' : temperatura_max,
                         'Temperatura Media' : temperatura_media,
                         'Temperatura Minima' : temperatura_min }

                # Frame con los datos finales
                finalTemperatura = DataFrame(data)
                finalTemperatura.plot()
                plt.title("Gráfica de Temperaturas año: " + año)
                plt.xlabel("Mes")
                plt.ylabel("Grados Celsius")
                plt.savefig("/home/hugo/PycharmProjects/pintgrupo16/django/www/MeteoGaliciaDB/consulta/static/consulta/"
                            "imagenes/" + nombre_png + ".png")
                plt.close()
            elif( tipoGrafica == "tablaPrecipitaciones"):
                '''
                PRECIPITACIONES
                '''
                frame_pre = DataFrame(datos, columns = precipitacions, index = indice)
                # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
                frame_pre = frame_pre.iloc[0:12]
                # Borramos valores nulos
                frame_pre = frame_pre.dropna()
                # Convertimos los valores en floats
                frame_pre = frame_pre.p_mes.map(lambda x: float(x))
                # Frame con los datos finales y plot
                frame_pre.plot(kind = 'bar', color = 'b')
                plt.title("Histograma de Precipitaciones año: " + año)
                plt.xlabel("Mes")
                plt.ylabel("Litro por m²")
                plt.savefig("/home/hugo/PycharmProjects/pintgrupo16/django/www/MeteoGaliciaDB/consulta/static/consulta/"
                            "imagenes/" + nombre_png + ".png")
                plt.close()

            elif( tipoGrafica == "histogramaHumedad"):
                '''
                HUMEDAD RELATIVA
                '''
                frame_hm = DataFrame(datos, columns = humedad, index = indice)
                # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
                frame_hm = frame_hm.iloc[0:12]
                # Borramos valores nulos
                frame_hm = frame_hm.dropna()
                # Convertimos los valores en floats
                frame_hm = frame_hm.hr.map(lambda x: float(x))
                # Frame con los datos finales y plot
                frame_hm.plot(kind = 'barh', color = 'b')
                plt.title("Histograma de Humedad Relativa año: " + año)
                plt.xlabel("(%)")
                plt.ylabel("Mes")
                plt.savefig("/home/hugo/PycharmProjects/pintgrupo16/django/www/MeteoGaliciaDB/consulta/static/consulta/"
                            "imagenes/" + nombre_png + ".png")
                plt.close()

            elif( tipoGrafica == "rosaVientos"):
                '''
                VENTO
                '''
                frame_vento = DataFrame(datos, columns = vento, index = indice)
                # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
                frame_vento = frame_vento.iloc[0:12]
                # Borramos valores nulos
                frame_vento = frame_vento.dropna()
                # Limpiamos datos y obtenemos los grados completos del resultada
                frame_vento_dir = frame_vento.w_racha.map(lambda x: x.replace('(', '/')).map(lambda x: x.split('/')). \
                                      map(lambda x: x[0]).map(lambda x: float(x)) * 10
                # Limpiamos datos y pasamos a kilometros por hora
                frame_vento_vel = frame_vento.w_racha.map(lambda x: x.replace('(', '/')).map(lambda x: x.split('/')). \
                                      map(lambda x: x[1]).map(lambda x: float(x)) / 1000 * 3600

                ## Discretizamos el conjunto de valores en n intervalos,
                ## en este caso 8 intervalos
                datosbin = np.histogram(frame_vento_dir, bins = np.linspace(np.min(frame_vento_dir), np.max(frame_vento_dir), 9))[0]
                ## Los datos los queremos en tanto por ciento
                datosbin = datosbin * 100. / len(frame_vento_dir)
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
                plt.savefig("/home/hugo/PycharmProjects/pintgrupo16/django/www/MeteoGaliciaDB/consulta/static/consulta/"
                            "imagenes/" + nombre_png + ".png")
                plt.close()
            return render(request, 'consulta/resultado/imprimir.html', {'lugar': lugar,
                                                                        'respuesta3': peticion3.content,
                                                                        'Variables': variables_posibles,
                                                                        'grafica':tipoGrafica,
                                                                        'latitud': latitud,
                                                                        'longitud': longitud,
                                                                        'nombre_png': nombre_png})
        else:
            aviso = "¡¡¡Debe cubrir latitud y longitud o, de no hacerlo, indicar un lugar válido!!!"
            return render(request, 'consulta/formulario/form.html', {'form': form, 'aviso': aviso})
    return render(request, 'consulta/formulario/form.html', {'form': form})
