
Feature: Agregar Peliculas                                                                                                                                                                                                                                                          # \test\features\agregar_pelicula.feature:1
  Como un administrador de sistema de Renta de Películas                                                                                                                                                                                                                            # \test\features\agregar_pelicula.feature:2
  Quiero agregar películas a mi catalogo                                                                                                                                                                                                                                            # \test\features\agregar_pelicula.feature:3
  con los datos, titulo,sinopsis,clasificacion                                                                                                                                                                                                                                      # \test\features\agregar_pelicula.feature:4
  duracion,genero,estreno y actores                                                                                                                                                                                                                                                 # \test\features\agregar_pelicula.feature:5
  Para mantener mi inventario de peliculas actualizado.                                                                                                                                                                                                                             # \test\features\agregar_pelicula.feature:6

  Scenario: Agregar Pelicula                                                                                                                                                                                                                                                        # \test\features\agregar_pelicula.feature:8
    Dado que ingreso al modulo nueva pelicula y ingreso el titulo "Criaturas Fantasticas", la sinopsis "pelicula chida",seleccionola clasificacion "A", ingreso duracion "250 min", selecciono el genero"Aventura", selecciono el estreno "Si",ingreso los actores "Actor1, Actor2" # \test\features\agregar_pelicula.feature:9
    Cuando presiono el boton "Agregar"                                                                                                                                                                                                                                              # \test\features\agregar_pelicula.feature:10
    Entonces puedo ver la pelicula "Criaturas Fantasticas" en la lista de peliculas.                                                                                                                                                                                                # \test\features\agregar_pelicula.feature:11

1 feature (0 passed)
1 scenario (0 passed)
3 steps (3 undefined, 0 passed)

You can implement step definitions for undefined steps with these snippets:

# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Dado que ingreso al modulo nueva pelicula y ingreso el titulo "([^"]*)", la sinopsis "([^"]*)",seleccionola clasificacion "([^"]*)", ingreso duracion "([^"]*)", selecciono el genero"([^"]*)", selecciono el estreno "([^"]*)",ingreso los actores "([^"]*)"')
def dado_que_ingreso_al_modulo_nueva_pelicula_y_ingreso_el_titulo_group1_la_sinopsis_group2_seleccionola_clasificacion_group3_ingreso_duracion_group4_selecciono_el_generogroup5_selecciono_el_estreno_group6_ingreso_los_actores_group7(step, group1, group2, group3, group4, group5, group6, group7):
    assert False, 'This step must be implemented'
@step(u'Cuando presiono el boton "([^"]*)"')
def cuando_presiono_el_boton_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Entonces puedo ver la pelicula "([^"]*)" en la lista de peliculas.')
def entonces_puedo_ver_la_pelicula_group1_en_la_lista_de_peliculas(step, group1):
    assert False, 'This step must be implemented'
