
Feature: Rentar Pelicula                                                                                                   # \test\features\rentar_pelicula.feature:1
  Como cliente del sistema de Renta de Películas                                                                           # \test\features\rentar_pelicula.feature:2
  Quiero rentar una pelicula                                                                                               # \test\features\rentar_pelicula.feature:3
  Para poder relajarme después de terminar el examen de Testing.                                                           # \test\features\rentar_pelicula.feature:4

  Scenario: Rentar Pelicula Estreno                                                                                        # \test\features\rentar_pelicula.feature:6
    Dado que selecciono la pelicula "Criaturas Fantasticas"                                                                # \test\features\rentar_pelicula.feature:7
    Cuando presiono el boton "Rentar"                                                                                      # \test\features\rentar_pelicula.feature:8
    Entonces puedo la fecha y hora "07/12/2016 12:00", la pelicula "Criaturas Fantasticas", fecha de entrega "08/12/2016". # \test\features\rentar_pelicula.feature:9

  Scenario: Rentar Pelicula                                                                                                # \test\features\rentar_pelicula.feature:6
    Dado que selecciono la pelicula "Hercules"                                                                             # \test\features\rentar_pelicula.feature:12
    Cuando presiono el boton "Rentar"                                                                                      # \test\features\rentar_pelicula.feature:8
    Entonces puedo la fecha y hora "07/12/2016 12:30", la pelicula "Hercules", fecha de entrega "10/12/2016".              # \test\features\rentar_pelicula.feature:14

1 feature (0 passed)
2 scenarios (0 passed)
6 steps (6 undefined, 0 passed)

You can implement step definitions for undefined steps with these snippets:

# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Dado que selecciono la pelicula "([^"]*)"')
def dado_que_selecciono_la_pelicula_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Cuando presiono el boton "([^"]*)"')
def cuando_presiono_el_boton_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Entonces puedo la fecha y hora "([^"]*)", la pelicula "([^"]*)", fecha de entrega "([^"]*)".')
def entonces_puedo_la_fecha_y_hora_group1_la_pelicula_group2_fecha_de_entrega_group3(step, group1, group2, group3):
    assert False, 'This step must be implemented'
