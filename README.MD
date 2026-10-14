# 1er Trabajo Practico de Procesamiento de datos:

## Desarrollo:
Para realizar este trabajo voy a utilizar la estructura Medallion, separando en 3 capas el proceso de los datos.
El dataset que voy a utilizar es que por defecto el profesor incluye en la consigna: **Desastres Nataturales 1970 - 2021**


### Estrutura del proyecto
La estructura que usare para poder seguir con la estrutura Medallion y aparte de ir escalando el proceso del dataset, tambien voy a seperar por modulos a cada proceso, que los voy a guardar en la carpeta scripts, asi como los dataset van a estar en la carpeta data, voy a ir llamando los procesos todo desde el archivo main, en el cual estaran importados los respectivos modulos de los procesos.

### Capa Bronce

En esta capa importe el archivo crudo desde la carpeta sources, aca voy a hacer la ingesta y visualizacion del dataframe, analizando la estructura, tipos de datos que contienen cada columna, cantidad de datos nulos promedios y valores unicos de las columnas que me serviran para el proceso de analisis mas adelante segun la consigna.

### Capa Plata

