# Tipo petición http://servizos.meteogalicia.es/apiv3/findPlaces?location=oure&API_KEY=***

import urllib3
import json
import requests

# Consultamos el lugar al usuario
print("Selecciona el lugar para obtener sus datos: ")
lugar = input()

# Preparamos los datos de la petición
api_code = 'tcZwyEj10Lb5W11usQMSM52QIlCutCCI64LfHv8AeuJsp9aE1F16tsn4yvdK0R52'
parametros = {'location': lugar, 'API_KEY': api_code}
url = 'http://servizos.meteogalicia.es/apiv3/findPlaces'

# Enviamos la peticion
peticion = requests.get(url, parametros)

# Obtenemos la respuesta
'''
Nos devuelve un json con la siguiente estructura

{
    "type" : "FeatureCollection",
    "crs" : {
        "type" : "name",
        "properties" : {
            "name" : CRS
        }
    },
    "features" : FEATURES_ARRAY
}

{
    "type" : "Feature",
    "geometry" : {
        "type" : "Point",
        "coordinates": [
            X,
            Y
        ]
    },
    "properties" : {
    "id" : ID,
    "name" : NAME,
    "municipality" : MUNICIPALITY,
    "province" : PROVINCE,
    "type" : TYPE
    }
}

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

'''
En google maps obtenemos un iframe tal que así

<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d11616.09153605781!2d-7.6873714500000006!3d43.292842449999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1ses!2ses!4v1492344844203" width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>

Tal que así nos sale Vilalba:

<iframe style="border: 0;" src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d11616.09153605781!2d-7.05321!3d43.21462!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1ses!2ses!4v1492344844203" width="600" height="450" frameborder="0" allowfullscreen="allowfullscreen"></iframe>


'''

# Ya para obtener la predicción de un punto en concreto
'''
http://servizos.meteogalicia.es/apiv3/getNumericForecastInfo?coords=-8.350573861318628,43.3697102138535&API_KEY=***

Y obtenemos una respuesta con la siguiente estructura:



    Variable sky_state:

    {
      "name": VARIABLE_NAME,
      "model": MODEL_NAME,
      "grid": GRID_NAME,
      "geometry": {
        "type": "Point",
        "coordinates": [
          X,
          Y
        ]
      "values": VALUES_ARRAY
    }

    Variable wind:

    {
      "name": VARIABLE_NAME,
      "model": MODEL_NAME,
      "grid": GRID_NAME,
      "moduleUnits": MODULE_UNIT_NAME,
      "directionUnits": DIRECTION_UNIT_NAME,
      "geometry": {
        "type": "Point",
        "coordinates": [
          X,
          Y
        ]
      "values": VALUES_ARRAY
    }

    Resto de las variables:

    {
      "name": VARIABLE_NAME,
      "model": MODEL_NAME,
      "grid": GRID_NAME,
      "units": UNIT_NAME,
      "geometry": {
        "type": "Point",
        "coordinates": [
          X,
          Y
        ]
      "values": VALUES_ARRAY
    }
'''

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
print("La respuesta HTTP obtenida para el tiempo de las coordenadas y variables que le pasamos es: {}".format(
    peticion3.status_code))
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

http://servizos.meteogalicia.es/apiv3/getNumericForecastInfo?coords=-7.13934,43.23871&format=text/html&API_KEY=tcZwyEj10Lb5W11usQMSM52QIlCutCCI64LfHv8AeuJsp9aE1F16tsn4yvdK0R52&variables=temperature

Desde esta url podemos ver lo que nos devuelve el json mejor que desde terminal...

http://codebeautify.org/jsonviewer

--> La consulta para que nos devuelva json y no html como arriba es tal que así:

http://servizos.meteogalicia.es/apiv3/getNumericForecastInfo?coords=-7.13934,43.23871&format=application/html&API_KEY=tcZwyEj10Lb5W11usQMSM52QIlCutCCI64LfHv8AeuJsp9aE1F16tsn4yvdK0R52&variables=temperature

Lo que obtenemos es esto:


{
	"type": "FeatureCollection",
	"crs": {
		"type": "name",
		"properties": {
			"name": "urn:ogc:def:crs:OGC:1.3:CRS84"
		}
	},
	"features": [
		{
			"type": "Feature",
			"geometry": {
				"type": "Point",
				"coordinates": [
					-7.13934,
					43.23871
				]
			},
			"properties": {
				"days": [
					{
						"timePeriod": {
							"begin": {
								"timeInstant": "2017-04-16T17:24:07+02"
							},
							"end": {
								"timeInstant": "2017-04-16T23:59:59+02"
							}
						},
						"variables": [
							{
								"name": "temperature",
								"model": "WRF",
								"grid": "04km",
								"units": "degc",
								"geometry": {
									"type": "Point",
									"coordinates": [
										-7.13934,
										43.23871
									]
								},
								"values": [
									{
										"timeInstant": "2017-04-16T18:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 14
									},
									{
										"timeInstant": "2017-04-16T19:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 12
									},
									{
										"timeInstant": "2017-04-16T20:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 12
									},
									{
										"timeInstant": "2017-04-16T21:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 10
									},
									{
										"timeInstant": "2017-04-16T22:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 9
									},
									{
										"timeInstant": "2017-04-16T23:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 8
									}
								]
							}
						]
					},
					{
						"timePeriod": {
							"begin": {
								"timeInstant": "2017-04-17T00:00:00+02"
							},
							"end": {
								"timeInstant": "2017-04-17T23:59:59+02"
							}
						},
						"variables": [
							{
								"name": "temperature",
								"model": "WRF",
								"grid": "04km",
								"units": "degc",
								"geometry": {
									"type": "Point",
									"coordinates": [
										-7.13934,
										43.23871
									]
								},
								"values": [
									{
										"timeInstant": "2017-04-17T00:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 7
									},
									{
										"timeInstant": "2017-04-17T01:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 7
									},
									{
										"timeInstant": "2017-04-17T02:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 6
									},
									{
										"timeInstant": "2017-04-17T03:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 6
									},
									{
										"timeInstant": "2017-04-17T04:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 5
									},
									{
										"timeInstant": "2017-04-17T05:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 6
									},
									{
										"timeInstant": "2017-04-17T06:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 6
									},
									{
										"timeInstant": "2017-04-17T07:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 6
									},
									{
										"timeInstant": "2017-04-17T08:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 6
									},
									{
										"timeInstant": "2017-04-17T09:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 8
									},
									{
										"timeInstant": "2017-04-17T10:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 13
									},
									{
										"timeInstant": "2017-04-17T11:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 15
									},
									{
										"timeInstant": "2017-04-17T12:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 16
									},
									{
										"timeInstant": "2017-04-17T13:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 17
									},
									{
										"timeInstant": "2017-04-17T14:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 17
									},
									{
										"timeInstant": "2017-04-17T15:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 18
									},
									{
										"timeInstant": "2017-04-17T16:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 18
									},
									{
										"timeInstant": "2017-04-17T17:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 18
									},
									{
										"timeInstant": "2017-04-17T18:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 17
									},
									{
										"timeInstant": "2017-04-17T19:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 16
									},
									{
										"timeInstant": "2017-04-17T20:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 14
									},
									{
										"timeInstant": "2017-04-17T21:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 11
									},
									{
										"timeInstant": "2017-04-17T22:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 10
									},
									{
										"timeInstant": "2017-04-17T23:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 9
									}
								]
							}
						]
					},
					{
						"timePeriod": {
							"begin": {
								"timeInstant": "2017-04-18T00:00:00+02"
							},
							"end": {
								"timeInstant": "2017-04-18T23:59:59+02"
							}
						},
						"variables": [
							{
								"name": "temperature",
								"model": "WRF",
								"grid": "04km",
								"units": "degc",
								"geometry": {
									"type": "Point",
									"coordinates": [
										-7.13934,
										43.23871
									]
								},
								"values": [
									{
										"timeInstant": "2017-04-18T00:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 8
									},
									{
										"timeInstant": "2017-04-18T01:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 8
									},
									{
										"timeInstant": "2017-04-18T02:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 8
									},
									{
										"timeInstant": "2017-04-18T03:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 6
									},
									{
										"timeInstant": "2017-04-18T04:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 6
									},
									{
										"timeInstant": "2017-04-18T05:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 5
									},
									{
										"timeInstant": "2017-04-18T06:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 5
									},
									{
										"timeInstant": "2017-04-18T07:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 5
									},
									{
										"timeInstant": "2017-04-18T08:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 5
									},
									{
										"timeInstant": "2017-04-18T09:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 8
									},
									{
										"timeInstant": "2017-04-18T10:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 10
									},
									{
										"timeInstant": "2017-04-18T11:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 14
									},
									{
										"timeInstant": "2017-04-18T12:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 16
									},
									{
										"timeInstant": "2017-04-18T13:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 18
									},
									{
										"timeInstant": "2017-04-18T14:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 19
									},
									{
										"timeInstant": "2017-04-18T15:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 20
									},
									{
										"timeInstant": "2017-04-18T16:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 19
									},
									{
										"timeInstant": "2017-04-18T17:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 18
									},
									{
										"timeInstant": "2017-04-18T18:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 18
									},
									{
										"timeInstant": "2017-04-18T19:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 16
									},
									{
										"timeInstant": "2017-04-18T20:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 14
									},
									{
										"timeInstant": "2017-04-18T21:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 12
									},
									{
										"timeInstant": "2017-04-18T22:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 11
									},
									{
										"timeInstant": "2017-04-18T23:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 11
									}
								]
							}
						]
					},
					{
						"timePeriod": {
							"begin": {
								"timeInstant": "2017-04-19T00:00:00+02"
							},
							"end": {
								"timeInstant": "2017-04-19T23:59:59+02"
							}
						},
						"variables": [
							{
								"name": "temperature",
								"model": "WRF",
								"grid": "04km",
								"units": "degc",
								"geometry": {
									"type": "Point",
									"coordinates": [
										-7.13934,
										43.23871
									]
								},
								"values": [
									{
										"timeInstant": "2017-04-19T00:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 10
									},
									{
										"timeInstant": "2017-04-19T01:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 10
									},
									{
										"timeInstant": "2017-04-19T02:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 9
									},
									{
										"timeInstant": "2017-04-19T03:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 8
									},
									{
										"timeInstant": "2017-04-19T04:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 7
									},
									{
										"timeInstant": "2017-04-19T05:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 6
									},
									{
										"timeInstant": "2017-04-19T06:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 5
									},
									{
										"timeInstant": "2017-04-19T07:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 4
									},
									{
										"timeInstant": "2017-04-19T08:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 4
									},
									{
										"timeInstant": "2017-04-19T09:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 7
									},
									{
										"timeInstant": "2017-04-19T10:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 9
									},
									{
										"timeInstant": "2017-04-19T11:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 12
									},
									{
										"timeInstant": "2017-04-19T12:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 14
									},
									{
										"timeInstant": "2017-04-19T13:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 15
									},
									{
										"timeInstant": "2017-04-19T14:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 15
									},
									{
										"timeInstant": "2017-04-19T15:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 16
									},
									{
										"timeInstant": "2017-04-19T16:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 16
									},
									{
										"timeInstant": "2017-04-19T17:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 15
									},
									{
										"timeInstant": "2017-04-19T18:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 14
									},
									{
										"timeInstant": "2017-04-19T19:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 13
									},
									{
										"timeInstant": "2017-04-19T20:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 11
									},
									{
										"timeInstant": "2017-04-19T21:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 8
									},
									{
										"timeInstant": "2017-04-19T22:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 8
									},
									{
										"timeInstant": "2017-04-19T23:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 7
									}
								]
							}
						]
					},
					{
						"timePeriod": {
							"begin": {
								"timeInstant": "2017-04-20T00:00:00+02"
							},
							"end": {
								"timeInstant": "2017-04-20T02:00:00+02"
							}
						},
						"variables": [
							{
								"name": "temperature",
								"model": "WRF",
								"grid": "04km",
								"units": "degc",
								"geometry": {
									"type": "Point",
									"coordinates": [
										-7.13934,
										43.23871
									]
								},
								"values": [
									{
										"timeInstant": "2017-04-20T00:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 7
									},
									{
										"timeInstant": "2017-04-20T01:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 7
									},
									{
										"timeInstant": "2017-04-20T02:00:00+02",
										"modelRun": "2017-04-16T02:00:00+02",
										"value": 7
									}
								]
							}
						]
					}
				]
			}
		}
	]
}



'''
