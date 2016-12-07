 Feature: Eliminar/Modificar
  Como un administrador de sistema de Renta de Películas
  Quiero ver la lista de peliculas de mi catalogo
  Para poder visualizar las peliculas en existencia y rentadas.

  Scenario: Eliminar Pelicula
  	Dado que selecciono la pelicula "Koizora"
  	Cuando pesiono el boton "Eliminar"
  	Entonces veo que la pelicula no esta en la lista de peliculas actualizada.

  Scenario: Modificar Pelicula
  	Dado que selecciono la pelicula "Hercules"
  	Cuando pesiono el boton "Modificar" y quito el estatus de "rentada"
  	Entonces veo que la pelicula ya no esta rentada en la lista de peliculas.
  	
