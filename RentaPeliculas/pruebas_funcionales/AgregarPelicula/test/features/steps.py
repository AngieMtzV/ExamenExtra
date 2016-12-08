
# -*- coding: utf-8 -*-
from lettuce import step,world
from selenium import webdriver

@step(u'Dado que ingreso al modulo nueva pelicula y ingreso el titulo "([^"]*)", la sinopsis "([^"]*)",seleccionola clasificacion "([^"]*)", ingreso duracion "([^"]*)", selecciono el genero"([^"]*)", selecciono el estreno "([^"]*)",ingreso los actores "([^"]*)"')
def dado_que_ingreso_al_modulo_nueva_pelicula_y_ingreso_el_titulo_group1_la_sinopsis_group2_seleccionola_clasificacion_group3_ingreso_duracion_group4_selecciono_el_generogroup5_selecciono_el_estreno_group6_ingreso_los_actores_group7(step, titulo, sinopsis, clasificacion, duracion, genero, estreno, actores,renta):
   	world.driver = webdriver.Chrome()
   	world.driver.get("http://192.168.33.10:8000/peliculas/nueva")
   	campo_titulo = world.driver.find_element_by_id('id_titulo')
	campo_sinopsis = world.driver.find_element_by_id('id_sinopsis')
	selec_clasif = world.driver.find_element_by_id('id_clasificacion')
	campo_duracion = world.driver.find_element_by_id('id_duracion')
	select_genero = world.driver.find_element_by_id('id_genero')
	select_estreno = world.driver.find_element_by_id('id_estreno')
	select_actor = world.driver.find_element_by_id('id_actores')
	select_renta = world.driver.find_element_by_id('id_rentada')

	titulo = "" if titulo == " " else titulo
	sinopsis = "" if sinopsis == " " else sinopsis
	campo_duracion = "" if duracion == " " else duracion
	campo_titulo.send_keys(titulo)
	campo_sinopsis.send_keys(sinopsis)
	selec_clasif.click()
	campo_duracion.send_keys(duracion)
	options = select_clasif.find_elements_by_tag_name('option')
	for option in options:
		if option.text == clasificacion:
			option.click()
			break
	options1 = select_genero.find_elements_by_tag_name('option')
	for option in options:
		if option.text == genero:
			option.click()
			break
	options2 = select_actor.find_elements_by_tag_name('option')
	for option in options:
		if option.text == actores:
			option.click()
			break
	selec_renta.click()  

@step(u'Cuando presiono el boton "([^"]*)"')
def cuando_presiono_el_boton_group1(step, boton):
	boton = world.driver.find_element_by_partial_link_text("Guardar").click()

@step(u'Entonces puedo ver la pelicula "([^"]*)" en la lista de peliculas.')
def entonces_puedo_ver_la_pelicula_group1_en_la_lista_de_peliculas(step, group1):

    assert False, 'This step must be implemented'
