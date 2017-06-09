# -*- coding: utf-8 -*-

"""
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaWd1ZWxvdXZpbmhhQGdtYWlsLmNvbSIsImp0aSI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsImV4cCI6MTQ5OTE2MjExNiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE0OTEzODYxMTYsInVzZXJJZCI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsInJvbGUiOiIifQ.w0OazTbsiZdI5YQXCMIRnny_f0TwWF7leFvik1WeA8s
"""


import requests
import json
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import math

# Datos comunes (API_KEY)
querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaWd1ZWxvdXZpbmhhQGdtYWlsLmNvbSIsImp0aSI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsImV4cCI6MTQ5OTE2MjExNiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE0OTEzODYxMTYsInVzZXJJZCI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsInJvbGUiOiIifQ.w0OazTbsiZdI5YQXCMIRnny_f0TwWF7leFvik1WeA8s"}

# Pedimos los datos al ususario
# Con esto pedimos el idema directamente, pero seria deseable pedir lugar y buscar nosotros el idema
print("Inserte el lugar del que quiera obtener los datos: \n")
print(" Provincia ------------ Estacion ------------- Idema ")
print(" A Coruña       A Coruña (Estacion completa)   1387")
print(" A Coruña         A Coruña (Aeroporto)         1387E")
print(" A Coruña  Santiago de Compostela (Labacolla)  1428")
print(" A Coruña             Cabo Vilán               1393")
print(" Lugo              Rozas (Aeródromo)           1505")
print(" Ourense       Ourense (Granxa Deputación)     1690A")
print(" Pontevedra        Pontevedra (Mourente)       1484C")
print(" Pontevedra           Vigo (Peinador)          1495")
idema = str(input())


analisis = str(input("Desea un analisis mensual/anual (1) o diario (2): \n"))

# Anuales
if (analisis == "1"):
    anho = str(input("De que año desea hacer la comparacion de datos (1931 - 2016): \n"))
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/mensualesanuales/datos/anioini/" + anho + "/aniofin/" + anho + "/estacion/" + idema
    response = requests.request("GET" , url ,params = querystring, verify = False)
    #print(response.text)
    cont = json.loads(response.text)
    #print(cont)
    cont = cont['datos']
    #print(cont)
    # Obtenemos los datos que nos interesan y los pasamos a formato json
    response = requests.request("GET", cont, verify = False)
    #print(response.text)
    datos = json.loads(response.text)
    #print(datos)
    """
    ANALISIS DE DATOS CON PANDAS
    """

    temperaturas = [ 'tm_mes', 'ta_max', 'ta_min', 'fecha', 'indicativo']

    estado_ceo = ['n_cub', 'n_des', 'n_nub']

    precipitacions = ['p_mes']

    vento = ['w_med', 'w_racha']

    humedad = ['hr']

    cota_nieve = ['n_nie', 'n_gra']

    cols = [ 'tm_mes', 'ta_max', 'ta_min', 'fecha', 'indicativo', 'n_cub', 'n_des', 'n_nub', 'p_mes',
    'w_med', 'w_racha', 'hr', 'n_nie', 'n_gra']

    indice = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'Resumen']


    #frame = DataFrame(datos, index = indice)
    '''
    TEMPERATURAS
    '''
    # Creamos el DataFrame
    frame_tem = DataFrame(datos, columns = temperaturas, index = indice)
    # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
    frame_tem = frame_tem.iloc[0:12]
    print(frame_tem)

    #Procedemos a limpiar las filas del DataFrame
    temperatura_max = frame_tem.ta_max.map(lambda x: x.replace('(', ',')).map(lambda x: x.split(',')).map(lambda x: x[0]).map(lambda x: float(x))
    temperatura_min = frame_tem.ta_min.map(lambda x: x.replace('(', ',')).map(lambda x: x.split(',')).map(lambda x: x[0]).map(lambda x: float(x))
    temperatura_media = frame_tem.tm_mes
    temperatura_fechas = frame_tem.fecha.map(lambda x: x.replace('-', ',')).map(lambda x: x.split(',')).map(lambda x: x[1])

    data = { 'Temperatura Maxima' : temperatura_max,
             'Temperatura Media' : temperatura_media,
             'Temperatura Minima' : temperatura_min }

    finalTemperatura = DataFrame(data)
    print(finalTemperatura)

    '''
    ESTADO CEO
    '''
    # Creamos el DataFrame
    frame_ceo = DataFrame(datos, columns = estado_ceo, index = indice)
    # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
    # En este caso puede que nos sirva de utilidad esta fila
    frame_ceo = frame_ceo.iloc[0:12]
    print(frame_ceo)


    # En este apartado podemos mostrar graficas de sectores o barras multiples
    # no se cual se adpatara mejor

    '''
    PRECIPITACIONES
    '''
    frame_pre = DataFrame(datos, columns = precipitacions, index = indice)
    # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
    frame_pre = frame_pre.iloc[0:12]
    frame_pre = frame_pre.p_mes.map(lambda x: float(x))
    print(frame_pre)

    '''
    VENTO
    '''
    frame_vento = DataFrame(datos, columns = vento, index = indice)
    # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
    frame_vento = frame_vento.iloc[0:12]
    print(frame_vento)
    frame_vento = frame_vento.dropna()

    # Limpiamos datos y obtenemos los grados completos del resultada
    frame_vento_dir = frame_vento.w_racha.map(lambda x: x.replace('(', '/')).map(lambda x: x.split('/')).map(lambda x: x[0]).map(lambda x: float(x)) * 10
    # Limpiamos datos y pasamos a kilometros por hora
    frame_vento_vel = frame_vento.w_racha.map(lambda x: x.replace('(', '/')).map(lambda x: x.split('/')).map(lambda x: x[1]).map(lambda x: float(x)) / 1000 * 3600

    print("dir \n")
    print(frame_vento_dir)
    print("vel \n")
    print(frame_vento_vel)

    '''
    HUMEDAD
    '''
    frame_hm = DataFrame(datos, columns = humedad, index = indice)
    # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
    frame_hm = frame_hm.iloc[0:12]
    print(frame_hm)


    '''
    COTA DE NEVE
    '''
    frame_cota = DataFrame(datos, columns = cota_nieve, index = indice)
    # Con esto eliminamos la fila resumen que no nos sirve en nustro caso
    frame_cota = frame_cota.iloc[0:12]
    print(frame_cota)


    '''
    GRAFICAS
    '''

    #### TEMPERATURAS
    finalTemperatura.plot()
    plt.title("Gráfica de Temperaturas año: " + anho)
    plt.xlabel("Mes")
    plt.ylabel("Grados Celsius")
    plt.savefig("grafica.png")

    #### RECIPITACIONES




    #### VIENTO
    ## Discretizamos el conjunto de valores en n intervalos,
    ## en este caso 8 intervalos
    datosbin = np.histogram(frame_vento_dir, bins = np.linspace(np.min(frame_vento_dir), np.max(frame_vento_dir), 9))[0]
    ## Los datos los queremos en tanto por ciento
    datosbin = datosbin * 100. / len(frame_vento_dir)
    ## Los datos los queremos en n direcciones/secciones/sectores,
    ## en este caso usamos 8 sectores de una circunferencia
    sect = np.array([90, 45, 0, 315, 270, 225, 180, 135]) * 2. * math.pi / 360.
    nombresect = ['E','NE','N','NW','W','SW','S','SE']
    ## Dibujamos la rosa de frecuencias
    plt.axes([0.1,0.1,0.8,0.8], polar = True)
    plt.bar(sect, datosbin, align='center', width=45 * 2 * math.pi / 360.,
            facecolor='b', edgecolor='k', linewidth=2, alpha=0.5)
    plt.thetagrids(np.arange(0, 360, 45),nombresect,frac = 1.1, fontsize = 10)
    plt.title(u'Procedencia del viento en el año ' + anho)
    plt.show()






# Diarios  (Formato de fecha: 2016-06-01T10:00:00UTC)
elif (analisis == "2"):
    print("Esto aun no esta implementado illooooooo!!")


# Analisis incorrecto
else:
    print("Tipo de analisis incorrecto, aprende a leer mamón")
