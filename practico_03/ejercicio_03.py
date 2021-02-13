# Implementar la clase Persona que cumpla las siguientes condiciones:

# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.

# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.


from dataclasses import dataclass


class Persona:
    def __init__(self,
                 nombre: str,
                 edad: int,
                 sexo: str,
                 peso: float,
                 altura: float
                 ) -> None:
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def es_mayor_edad(self) -> bool:
        return self.edad >= 17


# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad() == True
assert Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad() == False
# NO MODIFICAR - FIN


# Re-Escribir utiliznaod DataClasses


@dataclass
class Persona:
    nombre: str
    edad: int
    sexo: str
    peso: float
    altura: float

    def es_mayor_edad(self) -> bool:
        return self.edad >= 18


# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad() == True
assert Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad() == False
# NO MODIFICAR - FIN
