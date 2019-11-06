# Práctica 1: Web scraping

## Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y Ciclo de Vida de los Datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web wortimmo.lu y generar un dataset.

## Miembros del equipo
La actividad ha sido realizada por **Elisa Fernández Maraver** (elisafm4) y **Francisco Javier Cea Barceló** (jceab) 

## Ficheros del código fuente

* **src/main.py**: código principal del programa.
* **src/auxiliar_func.py**: contiene las funciones auxiliares utilizadas: 'search_by' y 'get_data'.

### *Códigos necesarios para 'Search_by'*
A continuación se muestran los códigos principales utilizados para poder aplicar los filtros de lugar (*location*) y tipo de propiedad (*property_type*)
* *location*:
	+ País:
		+ Luxemburgo: *country-1*
		+ Francia: *country-5*
		+ España: *country-*
	+ Región: 
		+ Centro (LU): *region-3*
		+ Bremen (DE): *region-26*
	+ Localidad: 
		+ Luxemburgo - Centro: *city-577*
* *property_type*:
	+ Apartamento: *0*
	+ Bedroom: *1*
	+ Duplex: *2*
	+ Loft: *3*
	+ Studio: *5*
	+ Triplex: *6*
	+ Chalet: *8*
	+ Farm: *10*
	+ House: *12*
	+ Villa: *18*

## Bibliografía
* https://github.com/elisafm4/wortimmo_scraping
* Subirats, L., Calvo, M. (2019). Web Scraping. Editorial UOC.
* Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
* Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.
	
	
