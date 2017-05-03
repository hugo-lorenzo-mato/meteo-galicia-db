
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

print(cont)

url_2 = cont['datos']

print(url_2)

r = requests.request("GET", url_2, verify=False)

print(r.text)

datos = json.loads(r.text)

print(datos)



"""
EMPEZAMOS EL ANALISIS DE PANDAS
"""

# como datos es una lista tenemos que acceder a los 12 elementos (meses)


campos = [ 'ta_max', 'ta_min', 'fecha', 'indicativo']



frame = pd.DataFrame( datos, columns = campos)

print(frame)

# LIMPIAMOS EL CONTENIDO DEL DATAFRAME
"""
frame.agg( [('ta_max', lambda x:  x[i].replace(",",""))] )

print(frame)
"""

# DIBUJAMOS EL GRAFICO

df = DataFrame(np.random.rand(6, 4),index=['one', 'two', 'three', 'four', 'five', 'six'],columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df
df.plot(kind='bar', figsize=(15,10) )





## PRUEBA DE CONCEPTO


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

