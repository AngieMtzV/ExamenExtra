Feature: Agregar Peliculas
  Como un administrador de sistema de Renta de Películas
  Quiero agregar películas a mi catalogo
  con los datos, titulo,sinopsis,clasificacion
  duracion,genero,estreno y actores
  Para mantener mi inventario de peliculas actualizado.

  Scenario: Agregar Pelicula
  	Dado que ingreso al modulo nueva pelicula y ingreso el titulo "Criaturas Fantasticas", la sinopsis "pelicula chida",seleccionola clasificacion "A", ingreso duracion "250 min", selecciono el genero"Aventura", selecciono el estreno "Si",ingreso los actores "Actor1, Actor2"
  	Cuando presiono el boton "Agregar"
  	Entonces puedo ver la pelicula "Criaturas Fantasticas" en la lista de peliculas.
