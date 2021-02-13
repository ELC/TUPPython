# Implementar una función llamada actualizar_precio que tome una lista de
# articulos y al precio de cada articulo le sume un porcentaje.
# NO se debe modificar la clase ni los tests

from dataclasses import dataclass
from typing import List

# NO MODIFICAR - INICIO
@dataclass
class Articulo:
    _nombre: str
    _precio: float

    @property
    def nombre(self) -> str:
        return self._nombre.capitalize()

    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value

    @property
    def precio(self) -> float:
        return round(self._precio, 2)

    @precio.setter
    def precio(self, value: float) -> None:
        self._precio = value

# NO MODIFICAR - FIN


# MODIFICAR
from copy import deepcopy


def actualizar_precio(articulos: List[Articulo], porcentaje: float) -> List[Articulo]:
    nuevos = []
    for articulo in deepcopy(articulos):
        articulo.precio *= 1 + porcentaje_aumento / 100
        nuevos.append(articulo)
    return nuevos


# NO MODIFICAR - INICIO
nombres = ["sabana", "parlante", "computadora", "tasa", "botella", "celular"]
precios = [10.25, 5.258, 350.159, 25.99, 18.759, 215.231]

articulos = [Articulo(nombre, precio) for nombre, precio in zip(nombres, precios)]
porcentaje_aumento = 10

articulos_actualizados = actualizar_precio(articulos, porcentaje_aumento)
precios_desactualizados = [articulo.precio for articulo in articulos]
precios_actualizados = [articulo.precio for articulo in articulos_actualizados]

# Test Lista vacia
assert precios_actualizados

# Test de precios
for precio_viejo, precio_nuevo in zip(precios_desactualizados, precios_actualizados):
    assert precio_nuevo == round(precio_viejo * (1 + porcentaje_aumento / 100), 2)

# NO MODIFICAR - FIN
