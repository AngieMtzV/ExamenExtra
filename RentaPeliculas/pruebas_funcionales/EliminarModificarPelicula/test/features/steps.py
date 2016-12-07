
Feature: Eliminar/Modificar                                                    # \test\features\elimod_pelicula.feature:1
  Como un administrador de sistema de Renta de Películas                       # \test\features\elimod_pelicula.feature:2
  Quiero ver la lista de peliculas de mi catalogo                              # \test\features\elimod_pelicula.feature:3
  Para poder visualizar las peliculas en existencia y rentadas.                # \test\features\elimod_pelicula.feature:4

  Scenario: Eliminar Pelicula                                                  # \test\features\elimod_pelicula.feature:6
    Dado que selecciono la pelicula "Koizora"                                  # \test\features\elimod_pelicula.feature:7
    Cuando pesiono el boton "Eliminar"                                         # \test\features\elimod_pelicula.feature:8
    Entonces veo que la pelicula no esta en la lista de peliculas actualizada. # \test\features\elimod_pelicula.feature:9

  Scenario: Modificar Pelicula                                                 # \test\features\elimod_pelicula.feature:11
    Dado que selecciono la pelicula "Hercules"                                 # \test\features\elimod_pelicula.feature:12
    Cuando pesiono el boton "Modificar" y quito el estatus de "rentada"        # \test\features\elimod_pelicula.feature:13
    Entonces veo que la pelicula ya no esta rentada en la lista de peliculas.  # \test\features\elimod_pelicula.feature:14

1 feature (0 passed)
2 scenarios (0 passed)
6 steps (6 undefined, 0 passed)

You can implement step definitions for undefined steps with these snippets:

# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Dado que selecciono la pelicula "([^"]*)"')
def dado_que_selecciono_la_pelicula_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Cuando pesiono el boton "([^"]*)"')
def cuando_pesiono_el_boton_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Entonces veo que la pelicula no esta en la lista de peliculas actualizada.')
def entonces_veo_que_la_pelicula_no_esta_en_la_lista_de_peliculas_actualizada(step):
    assert False, 'This step must be implemented'
@step(u'Cuando pesiono el boton "([^"]*)" y quito el estatus de "([^"]*)"')
def cuando_pesiono_el_boton_group1_y_quito_el_estatus_de_group2(step, group1, group2):
    assert False, 'This step must be implemented'
@step(u'Entonces veo que la pelicula ya no esta rentada en la lista de peliculas.')
def entonces_veo_que_la_pelicula_ya_no_esta_rentada_en_la_lista_de_peliculas(step):
    assert False, 'This step must be implemented'
