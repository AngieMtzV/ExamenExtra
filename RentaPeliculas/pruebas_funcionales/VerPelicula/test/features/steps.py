from lettuce import step,world
from selenium import webdriver

@step(u'Dado que ingreso al sistema de Renta de Peliculas')
def dado_que_ingreso_al_sistema_de_renta_de_peliculas(step):
    world.driver = webdriver.Chrome()
    world.driver.get("http://192.168.33.10:8000/peliculas/index")
    assert "http://192.168.33.10:8000/peliculas/index" in world.driver.current_url

@step(u'Cuando ingreso al modulo lista peliculas')
def cuando_ingreso_al_modulo_lista_peliculas(step):
  time.sleep(3)
  button = world.driver.find_element_by_partial_link_text("Lista de Peliculas").click()
  time.sleep(3)
  assert False, 'This step must be implemented'
@step(u'Entonces puedo ver las listas de peliculas en existencia.')
def entonces_puedo_ver_las_listas_de_peliculas_en_existencia(step):
    tabla = world.driver.find_element_by_name("table")
    assert "admin/auth/user/" in world.driver.current_url
