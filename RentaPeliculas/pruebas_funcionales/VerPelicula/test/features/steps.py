
Feature: Ver Peliculas                                          # \test\features\ver_pelicula.feature:1
  Como un administrador de sistema de Renta de Películas        # \test\features\ver_pelicula.feature:2
  Quiero ver la lista de peliculas de mi catalogo               # \test\features\ver_pelicula.feature:3
  Para poder visualizar las peliculas en existencia y rentadas. # \test\features\ver_pelicula.feature:4

  Scenario: Ver Pelicula                                        # \test\features\ver_pelicula.feature:6
    Dado que ingreso al sistema de Renta de Peliculas           # \test\features\ver_pelicula.feature:7
    Cuando ingreso al modulo lista peliculas                    # \test\features\ver_pelicula.feature:8
    Entonces puedo ver las listas de peliculas en existencia.   # \test\features\ver_pelicula.feature:9

1 feature (0 passed)
1 scenario (0 passed)
3 steps (3 undefined, 0 passed)

You can implement step definitions for undefined steps with these snippets:

# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Dado que ingreso al sistema de Renta de Peliculas')
def dado_que_ingreso_al_sistema_de_renta_de_peliculas(step):
    assert False, 'This step must be implemented'
@step(u'Cuando ingreso al modulo lista peliculas')
def cuando_ingreso_al_modulo_lista_peliculas(step):
    assert False, 'This step must be implemented'
@step(u'Entonces puedo ver las listas de peliculas en existencia.')
def entonces_puedo_ver_las_listas_de_peliculas_en_existencia(step):
    assert False, 'This step must be implemented'
