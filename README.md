
<h3>I. Datos de los integrantes.</h3>

Miguel Ouviña Santamaría:    miguel.ouvina@udc.es

Hugo Manuel Lorenzo Mato:    hugo.lorenzo.mato@udc.es

Grupo 5.2

Laboratorio Miércoles 11:30


<h3>II. Funcionalidades a implementar.</h3>


Nuestra propuesta se basa en una aplicación desarrollada en Python que permitirá a los usuarios:


- 1) Consultar los datos del tiempo para el mismo día o un período posterior y para una zona o localidad determinada.

- 2) Se mostrará la anterior información acompañada de un estudio de los mismos datos obtenidos en el período de tiempo anterior que seleccione el usuario. Estos datos históricos se referirán a la zona o localidad que haya seleccionado previamente y a las mismas variables.

- 3) Se le permitirá además recibir esta información agregada en distintos formatos de representación gráfica (histogramas, circulares, etc.) e igualmente se le permitirá manipular las variables que desee observar o comparar.

- 4) Cuando el usuario no introduzca ninguna zona, se le mostrará la predicción más cercana a su posición.

- 5) El usuario podrá registrarse y loguearse en la web para realizar las consultas que desee.

- 6) El registro y acceso se podrá realizar también a través de algunas de las redes sociales con mayor número de seguidores: Facebook y Twitter.

La aplicación tendrá una aplicación web desarrollada con el framework para python Django.



<h3>III. Aspectos de la aplicación.</h3>

Mockups iniciales:

![image](Images%20md/image.png)

![image_1](Images%20md/image_1.png)

![image_2](Images%20md/image_2.png)

![image_3](Images%20md/image_3.png)

![image_4](Images%20md/image_4.png)


<h3>IV. Flujo de datos de la aplicación.</h3>

![image_5](Images%20md/image_5.png)

![image_6](Images%20md/image_6.png)

![image_7](Images%20md/image_7.png)

![image_8](Images%20md/image_8.png)



<h3>V. APIs utilizadas.</h3>

Las APIs que utilizaremos para nuestro proyecto son las siguientes:

[MeteoSIX](http://servizos.meteogalicia.gal/api_manual/gl/index.html) de Meteogalicia: a través de la misma obtendremos todos los datos vinculados a la previsión del tiempo para el mismo día o algunos de los posteriores que indique el usuario.

[AEMET Open Data](https://opendata.aemet.es/centrodedescargas/inicio) : nos serviremos de esta otra aplicación para obtener los datos históricos, ya que  MeteoSIX no mantiene un registro de datos históricos.

[Google Maps](https://developers.google.com/maps/web/?hl=es-419) : a la que acudiremos para representar el lugar o zona para la que se ha realizado la consulta.

También haremos un uso menor de otras APIs, como la de [Facebook](https://developers.facebook.com/docs/marketing-api/using-the-api) y [Twitter](https://dev.twitter.com/rest/public) para permitir el registro/acceso de usuarios.


<h3>VI. Uso de pandas.</h3>

Haremos uso de pandas para manipular los datos que iremos consiguiendo tanto de la API de MeteoSIX, como de AEMET fundamentalmente.

Es sobre estos últimos, sobre el conjunto de datos históricos, sobre los que más operaciones llevaremos a cabo con pandas; en concreto:

- Representación y variación anual de las distintas métricas que nos ofrecen las APIs como son la temperatura, temperatura máxima, temperatura mínima, velocidad del viento, etc.

- Estudiaremos las medias por distintos períodos de tiempo como año, lustros y décadas.

- También compararemos estos datos con el obtenido por la API de MeteoSIX. Permitirá poner en perspectiva histórica la previsión actual con los datos obtenidos en otra época.

- Para la visualización de los datos, utilizaremos también Pandas. Y dejaremos en manos del usuario la selección del tipo de gráfica a la que quiera recurrir: histogramas, representaciones lineales por años, diagramas de dispersión, etc.

