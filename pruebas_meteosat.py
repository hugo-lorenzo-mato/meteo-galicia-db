import json
import requests


'''
En Meteosat la consulta que nos interesa nos da la fecha sólo para
un día en concreto, por lo que para obtener el histórico, tenemos que lanzar
varias e ir obteniendo el dato año a año.

Esta es la URL que nos importa:


https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2010-06-02T00:00:00UTC/fechafin/2010-06-02T23:59:59UTC/estacion/1387/?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJodWdvLmxvcmVuem8ubWF0b0B1ZGMuZXMiLCJqdGkiOiI2YTc1MjVhMi0xMDI0LTQzNjktYWU5MS1kNzVmNjU4ZDg3ZTciLCJleHAiOjE1MDEwNzk5OTksImlzcyI6IkFFTUVUIiwiaWF0IjoxNDkzMzAzOTk5LCJ1c2VySWQiOiI2YTc1MjVhMi0xMDI0LTQzNjktYWU5MS1kNzVmNjU4ZDg3ZTciLCJyb2xlIjoiIn0.F02lR2Y0KN080CfUJxYWKinXFXgx0PWUOlMAssWiA38


'''
print("Selecciona el lugar para obtener sus datos: 1387 A Coruña ")


'''
key = open('meteosat_api_key','r')
clave = ""
for lineas in key:
	clave = clave + lineas

print("La clave es ====> {}".format(clave))
'''
#Vamos a introducir el siguiente rango de fechas

print("Desde que ao desea saber")
decision_anho = int(input())
print("¿Cuántos años atrás quiere obtener?: ")
decision_atras = int(input())

for i in range(decision_atras):
	j = i + 1
	anho = decision_anho
	anho_busqueda = anho - j
	fechainicio = "{}-06-02T00%3A00%3A00UTC".format(anho_busqueda)
	fechafinal = "{}-06-02T23%3A59%3A59UTC".format(anho_busqueda)
	estacion_clima = "1387"

	# Preparamos los datos de la petición
	url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{}/fechafin/{}/estacion/{}/".format(fechainicio,fechafinal,estacion_clima)
	api_code= "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJodWdvLmxvcmVuem8ubWF0b0B1ZGMuZXMiLCJqdGkiOiI2YTc1MjVhMi0xMDI0LTQzNjktYWU5MS1kNzVmNjU4ZDg3ZTciLCJleHAiOjE1MDEwNzk5OTksImlzcyI6IkFFTUVUIiwiaWF0IjoxNDkzMzAzOTk5LCJ1c2VySWQiOiI2YTc1MjVhMi0xMDI0LTQzNjktYWU5MS1kNzVmNjU4ZDg3ZTciLCJyb2xlIjoiIn0.F02lR2Y0KN080CfUJxYWKinXFXgx0PWUOlMAssWiA38"
	parametros = {"api_key": api_code}
	print(url)
	# Enviamos la peticion
	print()
	peticion = requests.get(url, params=parametros, verify=False)
	respuesta = json.loads(peticion.text)
	peticion = requests.get(respuesta["datos"], verify=False)
	respuesta = json.loads(peticion.text)
	# Forma de obtener un dato concreto. Nos devuelve una lista de json! ojo!
	print(respuesta[0])
