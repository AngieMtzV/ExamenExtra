Feature: Agregar Peliculas
  Como un administrador de sistema de Renta de Películas
  Quiero agregar películas a mi catalogo
  Para mantener mi inventario de peliculas actualizado.

  Scenario: Agregar Pelicula
  	Dado que ingreso al modulo nueva pelicula y anexo los siguientes datos
  	|titulo|sinopsis|clasificacion|duracion|genero|estreno|actores|
  	|Criaturas Fantasticas|pelicula chida|A|250 min|Aventura|Si|Actor1|
  	Cuando presiono el boton Guardar
  	Entonces puedo ver la pelicula en la lista de peliculas.