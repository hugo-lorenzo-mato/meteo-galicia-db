
"""
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaWd1ZWxvdXZpbmhhQGdtYWlsLmNvbSIsImp0aSI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsImV4cCI6MTQ5OTE2MjExNiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE0OTEzODYxMTYsInVzZXJJZCI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsInJvbGUiOiIifQ.w0OazTbsiZdI5YQXCMIRnny_f0TwWF7leFvik1WeA8s
"""

import requests
import json

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import sys

import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import pandas as pd
import numpy as np



print("Añade el año del que deseas ver el historico")
anho = input()

url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/mensualesanuales/datos/anioini/"+anho+"/aniofin/"+anho+"/estacion/1387"

querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaWd1ZWxvdXZpbmhhQGdtYWlsLmNvbSIsImp0aSI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsImV4cCI6MTQ5OTE2MjExNiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE0OTEzODYxMTYsInVzZXJJZCI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsInJvbGUiOiIifQ.w0OazTbsiZdI5YQXCMIRnny_f0TwWF7leFvik1WeA8s"}

payload = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaWd1ZWxvdXZpbmhhQGdtYWlsLmNvbSIsImp0aSI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsImV4cCI6MTQ5OTE2MjExNiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE0OTEzODYxMTYsInVzZXJJZCI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsInJvbGUiOiIifQ.w0OazTbsiZdI5YQXCMIRnny_f0TwWF7leFvik1WeA8s",
"anioini":"2000",
"aniofin":"2000",
"estacion":"1387"
}

response = requests.request("GET", url, params=querystring, verify=False)

print(response.text)

cont = json.loads(response.text)

#print(cont)

url_2 = cont['datos']

#print(url_2)

r = requests.request("GET", url_2, verify=False)

print(r.text)

datos = json.loads(r.text)

print(datos)



"""
EMPEZAMOS EL ANALISIS DE PANDAS
"""

# como datos es una lista tenemos que acceder a los 12 elementos (meses)

indice = {'0':'Enero', '1':'Febrero', '2':'Marzo', '3':'Abril', '4':'Mayo', '5':'Junio',
		  '6':'Julio', '7':'Agosto', '8':'Septiembre', '9':'Octubre', '10':'Noviembre', '11':'Diciembre'}


campos = [ 'ta_max', 'ta_min', 'fecha', 'indicativo']

frame = pd.DataFrame( datos, columns = campos)

camposP = ['p_mes', 'fecha']

frameP = pd.DataFrame(datos, columns = camposP)

print("Estos son los datos con los que se van a construir las graficas")
print(frame)

# LIMPIAMOS EL CONTENIDO DEL DATAFRAME

"""
lista = frame.ta_max.map(lambda x: x.replace('(', ',')).map(lambda x: x.split(','))
print(lista)
temperatura_max = lista.map(lambda x: x[0])
print(temperatura_max)
"""


temperatura_max = frame.ta_max.map(lambda x: x.replace('(', ',')).map(lambda x: x.split(',')).map(lambda x: x[0]).map(lambda x: float(x))
print(temperatura_max)

temperatura_min = frame.ta_min.map(lambda x: x.replace('(', ',')).map(lambda x: x.split(',')).map(lambda x: x[0]).map(lambda x: float(x))
print(temperatura_min)

fechas = frame.fecha.map(lambda x: x.replace('-', ',')).map(lambda x: x.split(',')).map(lambda x: x[1])
print(fechas)

framePrecipitacion = frameP.p_mes.map(lambda x: float(x))

data = { 'temp_max': temperatura_max,
		 'temp_min': temperatura_min }

framefinal = pd.DataFrame(data)#, index = ['1','2','3','4','5','6','7','8','9','10','11','12','13'])
print("******************************************************")
frameTemperatura = framefinal.iloc[0:12]
# Cambiamos los inidces numericos por el nombre de los meses del año
frameTemperatura.rename(index = indice, inplace = True)
print(frameTemperatura)


# DIBUJAMOS LA FUCK GRAFICA

# FRame temeperaturas
frameTemperatura.plot()

# Mostramos en pantalla
plt.show()

# Frame Precipitaciones
frame_P =framePrecipitacion.iloc[0:12]
frame_P.rename(index = indice, inplace = True)
frame_P.plot(kind='bar', color='blue', alpha=0.7 )
# Mostramos en pantalla
plt.show()

# map(lambda x: x.rstrip( "(")))

# DIBUJAMOS EL GRAFIC
"""
df = DataFrame(np.random.rand(6, 4),index=['one', 'two', 'three', 'four', 'five', 'six'],columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df
df.plot(kind='bar', figsize=(15,10) )


#ESTO ES UNA BURRADA PERO PARA MOSTRAR DE MOMENTO VALE

# Mostramos en pantalla
plt.show()
"""

## PRUEBA DE CONCEPTO

"""
print("Añade el año de inicio del que desea ver el historico")
ini = input()

print("Añade el año de fin del que desea ver el historico")
fin = input()

inicio = int(ini)

fini = int(fin)

dif = fini - inicio

while (dif != 0 ):


	url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/mensualesanuales/datos/anioini/"+str(inicio)+"/aniofin/"+str(inicio)+"/estacion/1387"

	inicio += 1

	dif -=1

	querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaWd1ZWxvdXZpbmhhQGdtYWlsLmNvbSIsImp0aSI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsImV4cCI6MTQ5OTE2MjExNiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE0OTEzODYxMTYsInVzZXJJZCI6ImY2MGY2ZTdhLTcxMmMtNDY0ZS05YTlmLTYzNWUyYjgyNThlYSIsInJvbGUiOiIifQ.w0OazTbsiZdI5YQXCMIRnny_f0TwWF7leFvik1WeA8s"}

	response = requests.request("GET", url, params=querystring, verify=False)

	#print(response.text)

	cont = json.loads(response.text)

	#print(cont)

	url_2 = cont['datos']

	#print(url_2)

	r = requests.request("GET", url_2, verify=False)

	#print(r.text)

	datos = json.loads(r.text)

	#print(datos)

	campos = [ 'ta_max', 'ta_min', 'fecha', 'indicativo']



	frame = pd.DataFrame( datos, columns = campos)

	print(frame)


print("FINNNNNNNNN!!!!!!!!!!!!!!!")


"""



"""
	********************************** EJEMPLO QUE VA A SER INCORPORADO YA A LA WEB  ******************************************************
"""
