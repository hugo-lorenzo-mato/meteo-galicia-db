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
fechainicio = "2010-06-02T00%3A00%3A00UTC" #"2008-07-02T00:00:00UTC"
fechafinal = "2010-06-02T23%3A59%3A59UTC" #"2008-07-02T23:59:59UTC"
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
#print(respuesta[0]["tmax"])




'''
respuesta = json.loads(peticion.text)

# Obtenemos nuestras coordenadas
longitud = str(respuesta['features'][0]['geometry']['coordinates'][0])
latitud = str(respuesta['features'][0]['geometry']['coordinates'][1])

# Imprimos la información que hemos obtenido
print("La respuesta HTTP obtenida para obtener las coordenadas es: {}".format(peticion.status_code))
print("La longitud es: {}".format(longitud))
print("La latitud es: {}".format(latitud))
print()

# Preparamos los datos de la petición
url = 'http://servizos.meteogalicia.es/apiv3/getNumericForecastInfo'
coordenadas = longitud + ',' + latitud
print("Las coordenadas juntas son: {}".format(coordenadas))
parametros2 = {'coords': coordenadas, 'API_KEY': api_code}
# Enviamos la peticion
peticion2 = requests.get(url, parametros2)

# Obtenemos la respuesta

respuesta2 = json.loads(peticion2.text)

# Imprimos la información que hemos obtenido
print("La respuesta HTTP obtenida para unas coordenadas sin especificar nada más es: {}".format(peticion2.status_code))
print()

# Si queremos obtener unos datos concretos, le pasamos como parámetros las variables que deseamos
variables = 'temperature'  # 'sky_state,temperature,precipitation_amount,wind'
parametros3 = {'coords': coordenadas, 'variables': variables, 'API_KEY': api_code}
# Enviamos la peticion
peticion3 = requests.get(url, parametros3)
# Obtenemos la respuesta
respuesta3 = json.loads(peticion3.text)
print("La respuesta HTTP obtenida para el tiempo de las coordenadas y variables que le pasamos es: {}".format(peticion3.status_code))
print()

# Vamos extrayendo los valores que nos interesan
valor1 = respuesta3['features'][0]['properties']['days'][0]['variables'][0]['values'][2]
print("El valor 1 obtenido es: {}".format(valor1))
print()


#Imprimimos todos los valores para la temperatura

# de 0 a longitud del array de días

for i in range(len(respuesta3['features'][0]['properties']['days'])):
    if i == 0:
        print()
        print("Valor para {} el mismo día que se consulta: ".format(variables))
    else:
        print()
        print("Valor para {} día +{}: ".format(variables, i))
    for j in range(len(respuesta3['features'][0]['properties']['days'][i]['variables'][0]['values'])):
        time_instant = str(respuesta3['features'][0]['properties']['days'][i]['variables'][0]['values'][j]['timeInstant'])
        if j == 0:
            print("Variable " + variables + " para el día: {}".format(time_instant[:10]))
        print(time_instant[11:19] + ' --> ' + str(respuesta3['features'][0]['properties']['days'][i]['variables'][0]['values'][j]['value']) + " ºC")
'''