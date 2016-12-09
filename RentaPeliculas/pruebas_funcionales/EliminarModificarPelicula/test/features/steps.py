# -*- coding: utf-8 -*-
from lettuce import step,world
from selenium import webdriver
import time

@step(u'Dado que quiero editar una pelicula de la lista')
def dado_que_quiero_editar_una_pelicula_de_la_lista(step):
	world.driver = webdriver.Chrome()
	world.driver.get('http://192.168.33.10:8000/peliculas/lista/')
	boton = world.driver.find_element_by_name('editar')
	boton.click()
	time.sleep(2)


@step(u'Cuando visualizo la pagina de edicion')
def cuando_visualizo_la_pagina_de_edicion(step):
	world.driver.get('http://192.168.33.10:8000/peliculas/7/modificar/')
	time.sleep(2)


@step(u'Entonces puedo editar el titulo de la pelicula')
def entonces_puedo_editar_el_titulo_de_la_pelicula(step):
	datos = step.columns
	titulo = world.driver.find_element_by_id('id_titulo').clear()
	titulo = world.driver.find_element_by_id('id_titulo').send_keys(datos[0].get('titulo'))
	boton = world.driver.find_element_by_tag_name('button')
	boton.click()

@step(u'Dado que quiero eliminar una pelicula de mi catalogo')
def dado_que_quiero_eliminar_una_pelicula_de_mi_catalogo(step):
	pass
    
@step(u'Cuando presiono el boton eliminar')
def cuando_presiono_el_boton_eliminar(step):
	boton = world.driver.find_element_by_name('borrar')
	boton.click()
    
@step(u'Entonces puedo eliminar una pelicula')
def entonces_puedo_eliminar_una_pelicula(step):
	world.driver.get('http://192.168.33.10:8000/peliculas/lista/')
   