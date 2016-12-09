 Feature: Eliminar/Modificar
  Como un administrador de sistema de Renta de Películas
  Quiero ver la lista de peliculas de mi catalogo
  Para poder visualizar las peliculas en existencia y rentadas.


Scenario: Editar peliculas
    Dado que quiero editar una pelicula de la lista
    Cuando visualizo la pagina de edicion
    Entonces puedo editar el titulo de la pelicula
    |titulo|sinopsis|clasificacion|duracion|genero|estreno|actores|
    |Hercules2|Dios del Olimpo|A|95min|Animacion|False|Disney|

Scenario: Eliminar peliculas
    Dado que quiero eliminar una pelicula de mi catalogo
    Cuando presiono el boton eliminar
    Entonces puedo eliminar una pelicula