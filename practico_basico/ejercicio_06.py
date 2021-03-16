"""Listas"""

"""
Inicializar una lista vacía y luego agregarle 4 elementos cualquiera

Restricción: Utilizar el método append
"""

# COMPLETAR - INICIO
lista_01 = []
lista_01.append(1)
lista_01.append("2")
lista_01.append(["tres"])
lista_01.append(4)
# COMPLETAR - FIN

assert len(lista_01) == 4


"""
Concatenar las siguientes listas

Restricción: Utilizar el método extend
"""

lista_a = [1, 2, 3]
lista_b = ["4", "5", "6"]
lista_c = ["siete", "ocho", "nueve"]

# COMPLETAR - INICIO
listas_concatenadas_01 = []
listas_concatenadas_01.extend(lista_a)
listas_concatenadas_01.extend(lista_b)
listas_concatenadas_01.extend(lista_c)
# COMPLETAR - FIN

assert listas_concatenadas_01 == [
    1, 2, 3, "4", "5", "6", "siete", "ocho", "nueve"]


"""
Agregar la variable variable_01 en la tercer posición de la lista lista_nueva

Restricción: Utilizar el método insert
"""

variable_01 = 2
lista_nueva = [0, 1, 3, 4]

# COMPLETAR - INICIO
lista_nueva.insert(2, variable_01)
# COMPLETAR - FIN

assert lista_nueva == [0, 1, 2, 3, 4]


"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista

Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]

# COMPLETAR - INICIO
lista_primero_y_ultimo = []
lista_primero_y_ultimo.append(lista[0])
lista_primero_y_ultimo.append(lista[-1])
# COMPLETAR - FIN

assert lista_primero_y_ultimo == ["ho", "la"]


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista

Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

# COMPLETAR - INICIO
lista_primeros = []
lista_primeros.append(lista[0])
lista_primeros.append(lista[1])
lista_primeros.append(lista[2])
# COMPLETAR - FIN

assert lista_primeros == ["ho", 3.1416, "la"]


"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista

Restricción: Utilizar indexado múltiple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

# COMPLETAR - INICIO
lista_primeros = lista[0:3]

# COMPLETAR - FIN

assert lista_primeros == ["ho", 3.1416, "la"]


"""
Armar una lista que contenga los primeros 2 y los últimos 2 elementos de la 
siguiente lista

Restricción: Utilizar el método extend junto al indexado múltiple
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

# COMPLETAR - INICIO
lista_primeros_y_ultimos = []
lista_primeros_y_ultimos.extend(lista[:2])
lista_primeros_y_ultimos.extend(lista[-2:])
# COMPLETAR - FIN

assert lista_primeros_y_ultimos == ["ho", "la","como", "estas?"]


"""
Ejercicios
Operaciones +, in, == (1 ejercicio para cada uno)
Funciones especiales any y all (1 ejercicio para cada una)
"""

