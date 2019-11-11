# Práctica 1 de tipología y ciencia de los datos.

Autor Emilio José Lucas Marcos

## Ficheros

### adv.py

Este es el único fichero creado y modificado por nosotros el resto son autogenerados tanto por env de python o por la librería scrapy al crear el proyecto.

El fichero adv es el encargado de llamar a las páginas web obtener los campos necesarios y guardarlos en un fichero csv, está formado por la clase QuotesSpider y dentro de esta la funcion parse que se encarga de llamar a las páginas web y recoger los datos necesarios tratarlos y guardarlos en un csv recursivamente.


Para poder generar el dataset debemos activar el entorno virtual con el siguiente comando #.\env\Scripts\activate# y después movernos hasta la carpeta pec del proyecto y ejecutar el siguiente comando #scrapy crawl pec#
