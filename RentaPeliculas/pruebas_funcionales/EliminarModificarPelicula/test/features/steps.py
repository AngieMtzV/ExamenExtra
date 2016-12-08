# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Dado que selecciono la pelicula "([^"]*)"')
def dado_que_selecciono_la_pelicula_group1(step, pelicula):
	titulo = world.driver.find_element_by_xpath('//table/tbody')

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
