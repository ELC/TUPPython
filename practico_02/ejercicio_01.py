# En este archivo se deben importar los módulos:
# - main.py as main
# - source/util.py as util
# - source/controller/controller.py as controller

# Los imports deben hacerse de forma tal que funcionen con TODAS las formas
# posibles de invocación (estando parados en la carpeta practico_01b):
# $PATH$/practico_01b> python ejercicio_01.py
# $PATH$/practico_01b> python -m ejercicio_01

# Referncia: https://docs.python.org/3/reference/import.html#the-import-system

import main
import source.util as util
import source.controller.controller as controller


# NO MODIFICAR - INICIO
assert main.name == "main"
assert util.name == "util"
assert controller.name == "controller"
# NO MODIFICAR - FIN

# El siguiente ejercicio se encuentra en source/ejercicio_02.py
