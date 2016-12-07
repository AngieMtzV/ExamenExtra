Feature: Rentar Pelicula
  Como cliente del sistema de Renta de Películas
  Quiero rentar una pelicula
  Para poder relajarme después de terminar el examen de Testing.

  Scenario: Rentar Pelicula Estreno
  	Dado que selecciono la pelicula "Criaturas Fantasticas"
  	Cuando presiono el boton "Rentar"
  	Entonces puedo la fecha y hora "07/12/2016 12:00", la pelicula "Criaturas Fantasticas", fecha de entrega "08/12/2016".

  Scenario: Rentar Pelicula 
  	Dado que selecciono la pelicula "Hercules"
  	Cuando presiono el boton "Rentar"
  	Entonces puedo la fecha y hora "07/12/2016 12:30", la pelicula "Hercules", fecha de entrega "10/12/2016".

