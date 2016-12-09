
# -*- coding: utf-8 -*-
from lettuce import step,world
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


@step(u'Dado que ingreso al modulo nueva pelicula y anexo los siguientes datos')
def dado_que_ingreso_al_modulo_nueva_pelicula_y_anexo_los_siguientes_datos(step):
	world.driver = webdriver.Chrome()
	world.driver.get("http://192.168.33.10:8000/peliculas/nueva")

	datos = step.columns
	world.driver.find_element_by_id('id_titulo').send_keys(datos[0].get('titulo'))
	world.driver.find_element_by_id('id_sinopsis').send_keys(datos[1].get('sinopsis'))
	clasif = Select(world.driver.find_element_by_id('id_clasificacion'))
	clasif = clasif.select_by_visible_text(step.hashes.first['clasificacion'])
	world.driver.find_element_by_id('id_duracion').send_keys(datos[3].get('duracion'))
	genero = Select(world.driver.find_element_by_id('id_genero'))
	genero = genero.select_by_visible_text(step.hashes.first['genero'])
	world.driver.find_element_by_xpath('//*[@id="id_estreno"]').click()
	actor = Select(world.driver.find_element_by_id('id_actores'))
	actor.select_by_visible_text(step.hashes.first['actores'])
	world.driver.find_element_by_xpath('/html/body/form/p[8]/label')



@step(u'Cuando presiono el boton Guardar')
def cuando_presiono_el_boton_agregar(step):
	boton = world.driver.find_element_by_tag_name('button')
	boton.click()
	time.sleep(2)
@step(u'Entonces puedo ver la pelicula en la lista de peliculas.')
def entonces_puedo_ver_la_pelicula_en_la_lista_de_peliculas(step):
	world.driver.get("http://192.168.33.10:8000/peliculas/lista/")