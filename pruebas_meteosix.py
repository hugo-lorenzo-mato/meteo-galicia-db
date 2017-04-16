# Tipo petición http://servizos.meteogalicia.es/apiv3/findPlaces?location=oure&API_KEY=***

import urllib3
import json
import requests

#Consultamos el lugar al usuario
print("Selecciona el lugar para obtener sus datos: ")
lugar = input()

#Preparamos los datos de la petición
api_code = 'tcZwyEj10Lb5W11usQMSM52QIlCutCCI64LfHv8AeuJsp9aE1F16tsn4yvdK0R52'
parametros = {'location':lugar,'API_KEY':api_code}
url = 'http://servizos.meteogalicia.es/apiv3/findPlaces'

#Enviamos la peticion
peticion = requests.get(url,parametros)

#Obtenemos la respuesta
'''
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

#Obtenemos nuestras coordenadas
longitud = str(respuesta['features'][0]['geometry']['coordinates'][0])
latitud  = str(respuesta['features'][0]['geometry']['coordinates'][1])

#Imprimos la información que hemos obtenido
print("La respuesta HTTP obtenida es: {}".format(peticion.status_code))
print(peticion.content)
print("La longitud es: {}".format(longitud))
print("La longitud es: {}".format(latitud))



